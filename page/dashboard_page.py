import streamlit as st
import pandas as pd

def render_dashboard_page():
    # حماية لمنع الـ KeyError: إذا لم يجد الاسم، نضع قيمة افتراضية "User" بأمان
    current_user = st.session_state.get('user_name', 'User')

    # الهيدر العلوي ترحيبي مع زر تسجيل الخروج
    col_title, col_logout = st.columns([4, 1])
    with col_title:
        st.markdown(f"# 📊 Welcome to Data Analytics Dashboard")
        st.write(f"Hello, **{current_user}**! Let's analyze your data.")
    
    with col_logout:
        st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)
        if st.button("Log out", key="logout_btn", use_container_width=True):
            st.session_state['page'] = 'login'
            st.session_state.pop('user_name', None)
            st.rerun()

    st.divider()

    # حاوية رفع الملف
    st.markdown("### 📥 Upload your Excel or CSV file")
    uploaded_file = st.file_uploader("Choose a file", type=["xlsx", "xls", "csv"])

    if uploaded_file is not None:
        try:
            # قراءة الملف ذكياً بناءً على نوعه
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)

            st.success("File uploaded successfully!")

            # الميزة 1: استعراض البيانات
            st.markdown("### 👀 Data Preview (First 5 Rows)")
            st.dataframe(df.head(), use_container_width=True)

            # الميزة 2: الإحصائيات الشاملة (ماكس، ميني، متوسط، وغيرها)
            st.markdown("### 📐 Comprehensive Statistical Analysis")
            
            # جلب الأعمدة الرقمية فقط للتحليل الإحصائي
            numeric_df = df.select_dtypes(include=['number'])
            
            if not numeric_df.empty:
                # حساب الإحصائيات الأساسية بـ Pandas بأسلوب منسق
                stats = numeric_df.describe().T
                stats = stats[['min', 'max', 'mean', '50%']].rename(columns={'50%': 'median'})
                st.dataframe(stats, use_container_width=True)
                
                # تحديث ذكي وحماية الـ Metrics من الأرقام الطويلة جداً كالـ ID
                st.markdown("#### 💡 Quick Metrics Overview")
                
                suitable_cols = [col for col in numeric_df.columns if 'id' not in col.lower() and 'code' not in col.lower()]
                target_col = suitable_cols[0] if suitable_cols else numeric_df.columns[0]
                
                max_val = numeric_df[target_col].max()
                min_val = numeric_df[target_col].min()
                mean_val = round(numeric_df[target_col].mean(), 2)
                
                max_str = f"{max_val:,}" if isinstance(max_val, (int, float)) else str(max_val)
                min_str = f"{min_val:,}" if isinstance(min_val, (int, float)) else str(min_val)
                mean_str = f"{mean_val:,}" if isinstance(mean_val, (int, float)) else str(mean_val)
                
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    if len(max_str) > 15:
                        st.info(f"**Highest ({target_col}):**\n{max_str}")
                    else:
                        st.metric(label=f"Highest ({target_col})", value=max_str)
                        
                with col2:
                    if len(min_str) > 15:
                        st.info(f"**Lowest ({target_col}):**\n{min_str}")
                    else:
                        st.metric(label=f"Lowest ({target_col})", value=min_str)
                        
                with col3:
                    if len(mean_str) > 15:
                        st.info(f"**Average ({target_col}):**\n{mean_str}")
                    else:
                        st.metric(label=f"Average ({target_col})", value=mean_str)
            else:
                st.warning("No numeric columns found in this file to calculate Max, Min, or Mean.")

            st.divider()

            # الميزة 3: الرسوم البيانية التفاعلية المحمية من التكرار
            st.markdown("### 📈 Interactive Data Visualization")
            
            all_columns = df.columns.tolist()
            
            col_x, col_y, col_type = st.columns(3)
            with col_x:
                x_axis = st.selectbox("Select X axis", all_columns, index=0)
            with col_y:
                num_cols = numeric_df.columns.tolist() if not numeric_df.empty else all_columns
                y_axis = st.selectbox("Select Y axis (Numeric Values)", num_cols, index=0)
            with col_type:
                chart_type = st.selectbox("Chart Type", ["Line Chart", "Bar Chart", "Area Chart"])

            # 🎯 الحل السحري: نعمل تجميع للبيانات وعمل متوسط (mean) في حال وجود تكرار لـ X axis
            # لكي نضمن عدم وجود duplicate entries في الفهرس نهائياً
            chart_data = df.groupby(x_axis)[y_axis].mean()

            # رسم المخطط بناءً على اختيار المستخدم وبأمان تام
            if chart_type == "Line Chart":
                st.line_chart(chart_data, use_container_width=True)
            elif chart_type == "Bar Chart":
                st.bar_chart(chart_data, use_container_width=True)
            elif chart_type == "Area Chart":
                st.area_chart(chart_data, use_container_width=True)

        except Exception as e:
            st.error(f"Error reading file: {str(e)}")
    else:
        st.info("💡 Please upload an Excel or CSV document above to populate the dynamic analytics dashboard.")