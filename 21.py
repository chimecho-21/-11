import streamlit as st

# 设置页面标题
st.set_page_config(page_title="旅游管理平台", layout="wide")

# 隐藏默认的Streamlit样式
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# 设置页面标题
st.title("我的主页")

# 创建顶部导航栏
col1, col2, col3 = st.columns([3, 1, 1])
with col2:
    st.markdown('<div style="text-align: center; font-size: 24px;">···</div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div style="text-align: center; font-size: 24px;">⚪</div>', unsafe_allow_html=True)

# 创建用户头像区域
st.markdown('<hr style="border: none; border-top: 1px solid #ddd; margin: 20px 0;">', unsafe_allow_html=True)

col_avatar, col_info = st.columns([1, 3])
with col_avatar:
    st.image("https://via.placeholder.com/150", width=150)  # 替换为你的头像图片路径
with col_info:
    st.markdown('<div style="font-size: 24px; margin-top: 20px;">郭婷婷</div>', unsafe_allow_html=True)

# 创建个人信息和我的收藏区域
col_personal, col_collection = st.columns(2)
with col_personal:
    st.markdown('<div style="text-align: center; padding: 15px; border-radius: 10px; background-color: #f5f5f5;">'
                '<span style="font-size: 18px;">个人信息</span>'
                '<div style="margin-top: 10px;">'
                '<svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24">'
                '<path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>'
                '<circle cx="12" cy="7" r="4"></circle>'
                '</svg>'
                '</div>'
                '</div>', unsafe_allow_html=True)
with col_collection:
    st.markdown('<div style="text-align: center; padding: 15px; border-radius: 10px; background-color: #f5f5f5;">'
                '<span style="font-size: 18px;">我的收藏</span>'
                '<div style="margin-top: 10px;">'
                '<svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24">'
                '<path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"></path>'
                '</svg>'
                '</div>'
                '</div>', unsafe_allow_html=True)

# 创建功能列表
st.markdown('<hr style="border: none; border-top: 1px solid #ddd; margin: 30px 0;">', unsafe_allow_html=True)

# 我的物品
st.markdown('<div style="display: flex; align-items: center; justify-content: space-between; padding: 15px; border-radius: 10px; background-color: #f9f9f9;">'
            '<div style="display: flex; align-items: center;">'
            '<svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24">'
            '<path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path>'
            '<polyline points="22,6 12,13 2,6"></polyline>'
            '</svg>'
            '<span style="margin-left: 10px; font-size: 18px;">我的物品</span>'
            '</div>'
            '<div>'
            '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24">'
            '<polyline points="9 18 15 12 9 6"></polyline>'
            '</svg>'
            '</div>'
            '</div>', unsafe_allow_html=True)

# 我的空间
st.markdown('<div style="display: flex; align-items: center; justify-content: space-between; padding: 15px; border-radius: 10px; background-color: #f9f9f9; margin-top: 10px;">'
            '<div style="display: flex; align-items: center;">'
            '<svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24">'
            '<rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>'
            '<line x1="3" y1="9" x2="21" y2="9"></line>'
            '</svg>'
            '<span style="margin-left: 10px; font-size: 18px;">我的空间</span>'
            '</div>'
            '<div>'
            '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24">'
            '<polyline points="9 18 15 12 9 6"></polyline>'
            '</svg>'
            '</div>'
            '</div>', unsafe_allow_html=True)

# 我的外包
st.markdown('<div style="display: flex; align-items: center; justify-content: space-between; padding: 15px; border-radius: 10px; background-color: #f9f9f9; margin-top: 10px;">'
            '<div style="display: flex; align-items: center;">'
            '<svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24">'
            '<path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>'
            '</svg>'
            '<span style="margin-left: 10px; font-size: 18px;">我的外包</span>'
            '</div>'
            '<div>'
            '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24">'
            '<polyline points="9 18 15 12 9 6"></polyline>'
            '</svg>'
            '</div>'
            '</div>', unsafe_allow_html=True)

# 我的公益
st.markdown('<div style="display: flex; align-items: center; justify-content: space-between; padding: 15px; border-radius: 10px; background-color: #f9f9f9; margin-top: 10px;">'
            '<div style="display: flex; align-items: center;">'
            '<svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24">'
            '<path d="M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18z"></path>'
            '<path d="M12 7v5l3 3"></path>'
            '</svg>'
            '<span style="margin-left: 10px; font-size: 18px;">我的公益</span>'
            '</div>'
            '<div>'
            '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24">'
            '<polyline points="9 18 15 12 9 6"></polyline>'
            '</svg>'
            '</div>'
            '</div>', unsafe_allow_html=True)

# 地址管理
st.markdown('<div style="display: flex; align-items: center; justify-content: space-between; padding: 15px; border-radius: 10px; background-color: #f9f9f9; margin-top: 10px;">'
            '<div style="display: flex; align-items: center;">'
            '<svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24">'
            '<path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>'
            '<circle cx="12" cy="10" r="3"></circle>'
            '</svg>'
            '<span style="margin-left: 10px; font-size: 18px;">地址管理</span>'
            '</div>'
            '<div>'
            '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24">'
            '<polyline points="9 18 15 12 9 6"></polyline>'
            '</svg>'
            '</div>'
            '</div>', unsafe_allow_html=True)

# 我的客服
st.markdown('<div style="display: flex; align-items: center; justify-content: space-between; padding: 15px; border-radius: 10px; background-color: #f9f9f9; margin-top: 10px;">'
            '<div style="display: flex; align-items: center;">'
            '<svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24">'
            '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path>'
            '</svg>'
            '<span style="margin-left: 10px; font-size: 18px;">我的客服</span>'
            '</div>'
            '<div>'
            '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24">'
            '<polyline points="9 18 15 12 9 6"></polyline>'
            '</svg>'
            '</div>'
            '</div>', unsafe_allow_html=True)

# 工具箱
st.markdown('<div style="display: flex; align-items: center; justify-content: space-between; padding: 15px; border-radius: 10px; background-color: #f9f9f9; margin-top: 10px;">'
            '<div style="display: flex; align-items: center;">'
            '<svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24">'
            '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"></path>'
            '</svg>'
            '<span style="margin-left: 10px; font-size: 18px;">工具箱</span>'
            '</div>'
            '<div>'
            '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24">'
            '<polyline points="9 18 15 12 9 6"></polyline>'
            '</svg>'
            '</div>'
            '</div>', unsafe_allow_html=True)

# 创建底部导航栏
# 创建底部导航栏
st.markdown('<hr style="border: none; border-top: 1px solid #ddd; margin: 30px 0;">', unsafe_allow_html=True)

# 创建底部导航栏的三个按钮，横着排列
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div style="text-align: center; padding: 10px;">'
                '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24">'
                '<path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V9z"></path>'
                '</svg>'
                '<div style="margin-top: 5px; font-size: 14px;">首页</div>'
                '</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div style="text-align: center; padding: 10px;">'
                '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24">'
                '<circle cx="12" cy="12" r="10"></circle>'
                '<line x1="12" y1="16" x2="12" y2="12"></line>'
                '<line x1="12" y1="8" x2="12.01" y2="8"></line>'
                '</svg>'
                '<div style="margin-top: 5px; font-size: 14px;">发布</div>'
                '</div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div style="text-align: center; padding: 10px;">'
                '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="red" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24">'
                '<circle cx="12" cy="12" r="10"></circle>'
                '<path d="M12 6v6l4 2"></path>'
                '</svg>'
                '<div style="margin-top: 5px; font-size: 14px;">我的</div>'
                '</div>', unsafe_allow_html=True)
