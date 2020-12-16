#!/bin/bash 

file="input-8"
n=$(wc -l < $file)

prog=($(cat $file))
alreadyDone=()

mkdir -p aoc8
i=0
while [[ $i -lt "${#prog[@]}" ]]; do
    case "${prog[$(($i))]}" in
        nop) head -n $i $file > "aoc8/input-8-$i"
             echo "jmp ${prog[$(($i + 1))]}" >> "aoc8/input-8-$i"
             tail -n "$(($n - $i - 1))" $file >> "aoc8/input-8-$i"
             ;;
        jmp) head -n $i $file > "input-8-$i"
             echo "nop ${prog[$(($i + 1))]}" >> "aoc8/input-8-$i"
             tail -n "$(($n - $i - 1))" $file >> "aoc8/input-8-$i"
             ;;
        *)
             ;;
    esac
    i=$(($i + 2))
done
    

for file in $(ls "aoc8"); do
    prog=($(cat "aoc8/$file"))
    
    eip=0
    acc=0
    while true; do
        # echo "${prog[$((2 * $eip))]}" "${prog[$((2 * $eip + 1))]}" "$acc" "$eip"
        if [[ " ${alreadyDone[@]} " =~ " ${eip} " ]]; then
            # echo $acc
            echo "c'est mort"
            break
        fi
        if [[ $eip = $(($n + 1)) ]]; then
            echo "$eip $n $acc $file"
        fi
        alreadyDone+=("$eip")
        case "${prog[$((2 * $eip))]}" in
            nop) eip=$(($eip + 1))
                 ;;
            jmp) eip=$(($eip + ${prog[$((2 * $eip + 1))]}))
                 ;;
            acc) acc=$(($acc + ${prog[$((2 * $eip + 1))]}))
                 eip=$(($eip + 1));
                 ;;
            *) echo "Fuck ${prog[$((2 * $eip))]}"
               ;;
        esac
    done
done
