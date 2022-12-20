import moviepy.editor as mp
import os


# Set the path to the folder containing the clips
folder_path = 'C:/Users/Ruiming Kang/Desktop/TikTokDownload-main/Download/like/反斗乐园的牛爷爷'

# Create a list of the file names of the clips
clip_filenames = [f for f in os.listdir(folder_path) if f.endswith('.mp4')]

# Set the path to the output folder where the filtered clips will be saved
output_folder_path = 'C:/Users/Ruiming Kang/Desktop/moviepy/output'



def increase_contrast(clip):
    def adjust_contrast(im):
        # Increase the contrast of the image
        px = im.load()
        for x in range(im.width):
            for y in range(im.height):
                r, g, b = px[x, y]
                px[x, y] = (int(r * 1.5), int(g * 1.5), int(b * 1.5))
        return im
    return clip.fl_image(adjust_contrast)

#filtered_clip = clip.fx(increase_contrast)


# Loop through the clips and apply the filter
for clip_filename in clip_filenames:
    # Load the clip
    clip = mp.VideoFileClip(os.path.join(folder_path, clip_filename))

    # Apply the filter
    #filtered_clip = clip.fx(mp.vfx.colorx, 0.5)
    filtered_clip = clip.fx(mp.vfx.blackwhite)


    # Save the filtered clip to the output folder
    filtered_clip.write_videofile(os.path.join(output_folder_path, clip_filename))