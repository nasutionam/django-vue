<template>
    <div class="question-actions">
        
        <router-link
                    :to="{ name: 'question-editor', params: { slug: slug} }"
                    class="btn btn-sm btn-outline-secondary mr-1"
                    >Edit
        </router-link>
        <button @click="deleteQuestion" class="btn btn-sm btn-danger">Delete</button>
    </div>
</template>

<script>
import { apiService } from "../common/api.service";
import swal from 'sweetalert';

export default {
    name: "QuestionActions",
    props: {
        slug: {
            type: String,
            required: true
        }
    },
    methods: {
        deleteQuestion() {
            let endpoint = `/api/questions/${this.slug}/`;
            swal({
                title: "Are you sure?",
                text: "Once deleted, you will not be able to recover this imaginary file!",
                icon: "warning",
                buttons: true,
                dangerMode: true,
            })
            .then(async (willDelete) => {
            if (willDelete) {
                await apiService(endpoint, "DELETE");
                this.$router.push("/")
                swal("Poof! Your imaginary file has been deleted!", {
                    icon: "success",
                });
            } else {
                swal("Your imaginary file is safe!");
            }
            });
            
        }
    }
}
</script>

<style>
    
</style>