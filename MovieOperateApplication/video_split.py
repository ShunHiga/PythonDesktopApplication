import os
import subprocess
from pydub import AudioSegment
from pydub.silence import detect_nonsilent

#FFmpegのパスを指定
FFMPEG_PATH = "ffmpeg"

#無音とみなすパラメータ
min_silence_len = 500
silence_thresh = -30

#動画を分割して保存する
def split_video(video_path, output_path):
	#出力フォルダがなければ生成
	if not os.path.exists(output_path):
		os.makedirs(output_path)
	#動画からWAVを抽出
	audio_file = video_path.replace(".mp4","") + ".wav"
	subprocess.run([
		FFMPEG_PATH, '-y', '-i', video_path, '-vn',audio_file
	])

	#無音部分を検出する
	pos_list = detect_silent(audio_file)

	for i, (start, end) in enumerate(pos_list):
		if end == 0: continue
		#分割した動画を出力ディレクトリに保存
		print("-", msec_to_time(start), 'to', msec_to_time(end))
		f = os.path.join(output_path, f"video_{i}.mp4")
		cmd = [
			FFMPEG_PATH, '-y', '-i' , video_path, '-ss',
			msec_to_time(start), "-to", msec_to_time(end), '-c',
			'copy', f
		]
		subprocess.run(cmd)

#音声ファイルを操作して無音部分を調べる
def detect_silent(audio_file):
	#WAVファイルの読み込み
	audio_segment = AudioSegment.from_file(audio_file)

	#無音以外の部分を検出
	nonsilent_parts = detect_nonsilent(
		audio_segment,
		min_silence_len=min_silence_len,
		silence_thresh=silence_thresh
	)
	#結果のリストを作成する
	pos_list = []
	pos_end = 0
	for _, p in nonsilent_parts:
		pos_list.append([pos_end, p])
		pos_end = p
	return pos_list

#ミリ秒を hh:mm:ss　形式に変換する関数を定義
def msec_to_time(miliseconds):
	hours, miliseconds = divmod(miliseconds, 3600000)
	minutes, miliseconds = divmod(miliseconds, 60000)
	seconds = miliseconds/1000
	return f"{int(hours):02d}:{int(minutes):02d}:{seconds:.03f}"

if __name__ == "__main__":
	video_path = "about-python.mp4"
	output_path = "./video_split_parts"
	split_video(video_path=video_path, output_path=output_path)