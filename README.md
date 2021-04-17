## Color Picker REST API

### _Using Django_
Make a color picker REST API.
Input will be a logo image, output will be 2 color values 
1. color of the image border
2. primary logo color


The api specification should be as the following -
Get request to your_api_endpoint with image src url as a attribute
For e.g. 

http://your_api_endpoint.com?src=https://storage.googleapis.com/bizupimg/profile_photo/kppl_logo.png


should return json 

{
'logo_border': '#00003F',
'dominant_color': '#00003F'
}

*Note: See `test_outputs.md` for outputs.*