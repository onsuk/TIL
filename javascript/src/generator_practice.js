function* generator(){
    const users = yield 'Test Users';
    return (users + " Correctly received");
}

const iterator1 = generator();
const iteration = iterator1.next();

iteration

iteration.value.then(
    resolvedValue => {
        resolvedValue

        const nextIteration = iterator1.next(resolvedValue);

        nextIteration
    }
)