<template>
    <div class="container">
        <div class="answer-bord">
            <p class="text-muted">
            <strong>Answered by: {{ answer.author }} <strong class="float-right text-primary">{{ likesCounter }} Likes</strong></strong>
            </p>
            <p>{{ answer.body }} </p>
            <p><small>{{ answer.created_at }} </small></p>
            <div v-if="isAnswerAuthor">
                    <router-link
                    :to="{ name: 'answer-editor', params: { id: answer.id } }"
                    class="btn btn-sm btn-outline-secondary mr-1"
                    >Edit
                  </router-link>
                <button @click="triggerDeleteAnswer" class="btn btn-sm btn-danger">Delete</button>
            </div>
            <div v-else>
                <button class="btn btn-sm"
                @click="toggleLike"
                :class="{
                    'btn-danger': userLikedAnswer,
                    'btn-outline-danger': !userLikedAnswer
                
                }">
                    <strong>Like {{ likesCounter }}</strong>
                </button>
            </div>
        </div>
    </div>
</template>

<script>
import { apiService } from "../common/api.service";
import swal from 'sweetalert';
export default {
    name: "AnswerComponent",
    props: {
        answer: {
            type: Object,
            required: true
        },
        requestUser: {
            type: String,
            required: true
        }
    },
    data() {
        return {
            userLikedAnswer: this.answer.user_has_voted,
            likesCounter: this.answer.likes_count
        }
    },
    computed: {
        isAnswerAuthor() {
            return this.answer.author === this.requestUser;
        }
    },
    methods: {
        toggleLike(){
            this.userLikedAnswer === false
            ? this.likeAnswer()
            : this.unLikeAnswer()
        },
        likeAnswer(){
            this.userLikedAnswer = true;
            this.likesCounter += 1;
            let endpoint = `/api/answers/${this.answer.id}/like/`;
            apiService(endpoint, "POST")

        },
        unLikeAnswer(){
            this.userLikedAnswer = false;
            this.likesCounter -= 1;
            let endpoint = `/api/answers/${this.answer.id}/like/`;
            apiService(endpoint, "DELETE")
        },
        triggerDeleteAnswer() {
            swal({
                title: "Are you sure?",
                text: "Once deleted, you will not be able to recover this imaginary file!",
                icon: "warning",
                buttons: true,
                dangerMode: true,
            })
            .then((willDelete) => {
            if (willDelete) {
                this.$emit("delete-answer", this.answer);
                swal("Poof! Your imaginary file has been deleted!", {
                    icon: "success",
                });
            } else {
                swal("Your imaginary file is safe!");
            }
            });
            
        }
    },
}
</script>

<style>
    .answer-bord {
        border: 1px solid rgba(0,0,0,0.1);
        padding: 10px;
        margin-bottom: 10px;
    }
</style>