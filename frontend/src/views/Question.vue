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

            <div v-if="userHasAnswered">
                <p class="answer-added" style="margin-left: 13px; color:lightgreen;">You've written an answer</p>
            </div>
            <div v-else-if="showForm">
                <form class="card" @submit.prevent="onSubmit">
                    <div class="card-header px-3">
                        Answer the Question
                    </div>
                    <div class="card-block">
                        <textarea rows="5" v-model="newAnswerBody" class="form-control" placeholder="Answer the Question"></textarea>
                    </div>
                    <div class="card-footer px-3">
                        <button type="submit" class="btn btn-sm btn-success">Submit your answer</button>
                    </div>
                </form>
                <p v-if="error" class="error mt-2">{{ error }}</p>
            </div>
            <div v-else>
                <button style="margin-left: 10px;" class="btn btn-primary btn-sm" @click="showForm = true">Answer the Question</button>
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
            anyAnswer: true,
            newAnswerBody: null,
            error: null,
            userHasAnswered: false,
            showForm: false
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
                    this.userHasAnswered = data.user_has_answered;
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
        },
        onSubmit() {
            if(this.newAnswerBody) {
                let endpoint = `/api/questions/${this.slug}/answer/`;
                apiService(endpoint, "POST", { body: this.newAnswerBody})
                    .then(data => {
                        this.answers.unshift(data);
                    })
                this.newAnswerBody = null;
                this.showForm = false;
                this.userHasAnswered = true;
                if(this.error) {
                    this.error = null;
                }
            } else {
                this.error = "You cannot send an empty message";
            }
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