import plotly.express as px
import plotly.graph_objects as go


# LINE CHART
#df = px.data.gapminder()
# df = px.data.gapminder().query("country =='Vietnam'")
#df = px.data.gapminder().query("country in ['Canada', 'Vietnam']")
# df = px.data.gapminder().query("continent == 'Asia'")
# print(df)

# fig = px.line(df, x="year", y = "lifeExp", color='country', markers=True,
#               labels={'lifeExp': 'Mức sống', 'year': 'Năm', 'country':'Đất nước'})
# fig.show()

#BAR CHART
# df = px.data.gapminder().query("country == 'Vietnam'")
# fig = px.bar(df, x='year', y='pop', hover_data=['lifeExp', 'gdpPercap'],
#              color='lifeExp', labels={'pop': 'Dân số', 'lifeExp':'Mức sống',
#                                       'year':'Năm','gdpPercap': 'GDP' })
# fig.show()


# GROUP BAR CHART
 
# animals = ['elephants', 'giraffes', 'monkey']
# fig = go.Figure(data = [
#     go.Bar(name ='Nam phi', x = animals, y = [20, 15, 34], text=[20, 15, 34],
#             textposition= 'auto'),
#     go.Bar(name='Nigeria', x=animals, y = [14, 19, 27], text=[14, 19, 27], 
#            textposition='auto')
# ])

# #fig.update_layout(barmode='group')
# fig.update_layout(barmode='stack')
# fig.show()

# PIE CHART
# df = px.data.gapminder().query("continent =='Europe'")
# df.loc[df['pop']< 2.e6, 'country'] = 'Other countries'

#fig = px.pie(df, values='pop', names='country', title = 'Dân số lục địa Châu Âu')
#fig = px.pie(df, values='pop', names='country', title = 'Dân số lục địa Châu Âu', hole=.3)
#fig = px.pie(df, values='pop', names='country', title = 'Dân số lục địa Châu Âu')
df = px.data.gapminder().query("continent =='Oceania'")
fig = go.Figure(data =[
    go.Pie(labels=df['country'], values=df['pop'], pull=[0, 0.8])
])
fig.show()