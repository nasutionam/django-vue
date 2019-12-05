<template>
    <div class="container">
        <div class="answer-bord">
            <p class="text-muted">
            <strong>Answered by: {{ answer.author }}</strong>
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
        </div>
    </div>
</template>

<script>
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
    computed: {
        isAnswerAuthor() {
            return this.answer.author === this.requestUser;
        }
    },
    methods: {
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