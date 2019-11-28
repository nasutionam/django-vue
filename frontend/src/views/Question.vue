<template>
    <div class="single-question mt-2"> 
    <div class="mt-5"></div>
        <div class="container">
            <div class="bord">
                <h2> {{ question.content }} </h2>
                <p class="mb-0">Posted by:
                    <span class="author-name">{{ question.author }}</span>
                </p>
                <p> <small> {{ question.created_at }} </small></p>
            </div>
            
        </div>    
    </div>
</template>

<script>
import { apiService } from "../common/api.service";

export default {
    name: "Question",
    props: {
        slug: {
            type: String,
            required: true
        }
    },
    data() {
        return  {
            question: {}
        }
    },
    methods: {

        setPageTitle(title){
            document.title = title;
        },

        getQuestionData() {
            let endpoint = `/api/questions/${this.slug}/`;
            apiService(endpoint)
                .then(data => {
                    this.question = data;
                    this.setPageTitle(data.content);
                })
        }
    },
    created() {
        this.getQuestionData()
        console.log(this.question)
    }
}
</script>

<style>
  .bord {
    border: 1px solid #DDD;
    margin: 10px;
    padding: 20px;
    border-radius: 5px;
  }
  .cont {
    margin-top: 20px;
    color: gray;
  }
</style>