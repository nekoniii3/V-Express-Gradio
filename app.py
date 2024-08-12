import gradio as gr
import os
import datetime
import inference

example1 = ["sample_data/ref1.jpg", "sample_data/ano.mp3"]
example2 = ["sample_data/ref2.jpg", "sample_data/rakugo.mp3"]

def fix_face_video(input_image, input_audio):

    dt = datetime.datetime.now() + datetime.timedelta(hours=9)
    fol_name = dt.strftime("%Y%m%d")
    file_name = dt.strftime("%H%M%S")

    out_video = "./output/" + fol_name+ "/fix_face_" + file_name + ".mp4"

    inference.fix_face(input_image, input_audio, out_video)

    return out_video

image = gr.Image(label="画像(image)", type="filepath")
audio = gr.File(label="音声(audio)", file_types=[".mp3", ".MP3"])
out_video = gr.Video(label="Fix Face Video")
btn = gr.Button("送信", variant="primary")

title = "V_Express"
description = "<div style='text-align: center;'><h3>画像と音声だけで生成できます。(Using only images and audio)"
description += "<br>This uses the following V-Express \"https://github.com/tencent-ailab/V-Express\"</h3></div>"

demo = gr.Interface(
    fn=fix_face_video,
    inputs=[image, audio],
    examples=[example1, example2],
    outputs=[out_video],
    title=title,
    submit_btn=btn,
    clear_btn=None,
    description=description,
    allow_flagging="never"
)

demo.queue()
demo.launch(share=True, debug=True)