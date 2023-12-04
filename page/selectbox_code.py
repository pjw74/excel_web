# def result_page(summary, score_sum):
#
#     selected_page = list(page_names_to_funcs.keys())[1]
#     page_names_to_funcs[selected_page]()
#     display_results(summary, score_sum)
#
# page_names_to_funcs = {
#     "Main Page": main_page,
#     "Result Page": partial(result_page, *main_page()),
# }
#
# selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
# page_names_to_funcs[selected_page]()