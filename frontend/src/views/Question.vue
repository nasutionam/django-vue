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
            <div>
                <p v-if="anyAnswer" class="mt-5" style="margin-left: 13px; color: gray;">The answers...</p>
                <p v-else class="mt-5" style="margin-left: 13px; color: gray;">No answer...</p>


                <AnswerComponent v-for="(answer, index) in answers" :key="index" :answer="answer" />
            </div>
        </div>    
    </div>
</template>

<script>
import { apiService } from "../common/api.service";
import AnswerComponent from "@/components/Answer.vue";

export default {
    name: "Question",
    props: {
        slug: {
            type: String,
            required: true
        }
    },
    components: {
         AnswerComponent
    },

    data() {
        return  {
            question: {},
            answers: [],
            anyAnswer: true
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
        },
        getQuestionAnswers() {
            let endpoint = `/api/questions/${this.slug}/answers/`;
            apiService(endpoint)
                .then(data => {
                    this.answers = data.results;
                    if(this.answers.length <= 0 ){
                        this.anyAnswer = false;
                    }
                })
        }
    },
    created() {
        this.getQuestionData();
        this.getQuestionAnswers();
        console.log(this.question);
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