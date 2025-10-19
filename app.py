from dotenv import load_dotenv

load_dotenv()

# Streamlitのインポート
import streamlit as st

# タイトル表示
st.title("LLMチャットアプリ")

# アプリ概要・操作説明
st.markdown("""
このWebアプリは、AI（LLM）に質問を投げかけて専門家として回答を得ることができます。\n
【使い方】\n
1. 質問内容を入力フォームに記入してください。\n2. 専門家の種類（A:不動産／B:マーケティング）を選択してください。\n3. 入力後、回答が画面に表示されます。\n
専門家の視点で、より的確な回答を得ることができます。
""")

# テキスト入力フォーム
user_input = st.text_input("質問を入力してください：")

# 専門家選択ラジオボタン
expert_type = st.radio("専門家の種類を選択してください：", ("A:不動産", "B:マーケティング"))

from langchain_openai import OpenAI
import os

# OpenAI APIキーの取得
openai_api_key = os.getenv("OPENAI_API_KEY")

# LLMの初期化
llm = OpenAI(openai_api_key=openai_api_key)

# 入力テキストと選択値を受け取り、LLMからの回答を返す関数
def get_llm_response(user_input, expert_type):
	if expert_type == "A:不動産":
		system_message = "あなたは不動産分野の専門家です。質問には不動産の専門家として回答してください。"
	else:
		system_message = "あなたはマーケティング分野の専門家です。質問にはマーケティングの専門家として回答してください。"

	from langchain.prompts import ChatPromptTemplate
	prompt = ChatPromptTemplate.from_messages([
		("system", system_message),
		("human", user_input)
	])
	response = llm(prompt.format())
	return response

# 入力がある場合、LLMに渡して回答を表示
if user_input:
	response = get_llm_response(user_input, expert_type)
	st.write("回答：")
	st.write(response)
