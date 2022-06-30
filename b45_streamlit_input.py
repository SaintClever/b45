import streamlit as st


st.header('{B45}')
st.write('Replacement keyword: {B45}')
st.write('---')


versions = st.text_input('Versions')
links = st.text_area('Links')
copy = st.text_area('Copy')
button = st.button('Build file')


links = links.split(', ')
versions = versions.split(', ')


if copy != '' and links != '' and versions != '' and len(links) == len(versions):
    if button == True:
        # print(copy, versions, links)
        for i in range(len(links)):
            data = copy.replace('{B45}', links[i])

            with open(f'{versions[i]}.html', 'w') as f:
                f.write(data)
        st.success('Files built!')