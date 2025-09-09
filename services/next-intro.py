from moviepy import ImageClip, AudioFileClip, CompositeVideoClip
from moviepy.video import fx as vfx

def create_video_with_dynamic_crossfade(
    image_files,
    audio_file,
    output_file,
    crossfade_ratio=0.15,
    max_crossfade=2,
    size=(1280, 720),
    fps=30,
):
    # Load audio
    audio = AudioFileClip(audio_file)
    audio_duration = audio.duration

    # Divide audio duration equally among images
    duration_per_image = audio_duration / len(image_files)

    # Crossfade = % of image duration (capped)
    crossfade_duration = min(duration_per_image * crossfade_ratio, max_crossfade)

    clips = []
    current_start = 0.0

    for idx, img_path in enumerate(image_files):
        # Base clip with resize and duration
        base = (
            ImageClip(img_path)
            .with_duration(duration_per_image)
            .with_position("center")
            .with_effects([vfx.Resize(height=size[1])])  # scale to fit height
        )

        # First clip: no crossfade
        if idx == 0:
            clip = base.with_start(current_start)
        else:
            # Overlap this clip with previous by crossfade_duration
            current_start += duration_per_image - crossfade_duration
            clip = base.with_start(current_start).with_effects([vfx.CrossFadeIn(crossfade_duration)])

        clips.append(clip)

    # Compute total video duration
    total_duration = current_start + duration_per_image

    # Composite with crossfades
    video = CompositeVideoClip(clips, size=size, bg_color=(0, 0, 0)).with_duration(total_duration)

    # Attach audio (trimmed to video length)
    final_video = video.with_audio(audio.with_duration(total_duration))

    # Export video
    final_video.write_videofile(output_file, fps=fps, codec="libx264", audio_codec="aac")


if __name__ == "__main__":
    images = [
        "images/next-basic.png"
    ]
    audio = "audio/Audio-9_8_2025_1.m4a"
    output = "output/next-intro.mp4"

    create_video_with_dynamic_crossfade(images, audio, output)
