import http from 'k6/http';
import {sleep} from 'k6';

export const options = {
    vus: 15,
    duration: '20s', // for CPU blocked task
};
export default function () {
    http.get('http://127.0.0.1:5000/cpu');
}