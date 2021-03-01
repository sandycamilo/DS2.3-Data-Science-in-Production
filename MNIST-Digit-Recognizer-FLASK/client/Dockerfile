FROM node:8.11.3 as node

# Add requirements.txt file 
COPY . .

ADD . /application

# Set working directory to previously added app directory
WORKDIR /application

# # Expose the port Flask is running on 
# EXPOSE 3000

# # Command to run application
# CMD ["npm", "start"]

RUN npm run build -- --prod --environment $env

FROM node:alpine

EXPOSE 3000
CMD ["npm", "start"]
