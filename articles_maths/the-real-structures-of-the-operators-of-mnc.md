# __The Real Structures of the Operators of $M_n(\mathbb{C})$, including Lie Algebras and Lie Groups__

## Introduction

**The question.** Which real structures does the operator space $\operatorname{End}(M_n(\mathbb{C}))$ carry, as an algebra, as a Lie algebra and as a group?

**The answer in one line.** The algebra has the real form $M_{n^2}(\mathbb{R})$ always and $M_{n^2/2}(\mathbb{H})$ for even $n$; the Lie algebra $\mathfrak{gl}_{n^2}$ has real dimension $2n^4$ with compact form $\mathfrak{u}(n^2)$ of dimension $n^4$; the group is $GL_{n^2}(\mathbb{C})$, with maximal compact $U(n^2)$.

**Why the article is needed.** The biquaternion article could say "the real structure is $M_4(\mathbb{R})$" and be done, because $n=2$ gives $n^2=4$ and the quaternionic form is also available. At general $n$ the two forms separate: the split form is always there and the quaternionic form needs $n$ even, so a statement that is true at $n=2$ becomes a statement with a parity condition.

**Boundaries.** The classification questions are *The Classification of the Structures of the Operators of $M_n(\mathbb{C})$*; the complex side is *The Complex Structures of the Operators of $M_n(\mathbb{C})$, including Lie Algebras and Lie Groups*; the compact group acting on the carrier is *The $SU(2)$ of $M_n(\mathbb{C})$ Acting on $n^2$ Dimensions*.

**Conventions.** $N=n^2$. The Hilbert–Schmidt space is $\mathbb{C}^N$ with the form $\langle X,Y\rangle=\operatorname{tr}(X^{*}Y)$. The column-stacking frame identifies $\operatorname{End}(M_n)$ with $M_N(\mathbb{C})$.

## The Real Form of the Algebra

**Proposition.** The operators with real matrix in the column-stacking frame form a real subalgebra isomorphic to $M_{n^2}(\mathbb{R})$, and it is the commutant of the entrywise conjugation $X\mapsto\bar X$ of the carrier.

*Proof.* $B^{\mathsf T}\otimes A$ is real exactly when $A$ and $B$ are real, and the matrices commuting with entrywise conjugation are exactly the real ones. $\square$

**The consequence for the families.** $L_A$, $R_B$ and $T_{A,B}$ are real in the frame exactly when the parameters are real. So the real form contains the real span of the three families, of real dimension $2n^2-1$, sitting inside $M_{n^2}(\mathbb{R})$ of real dimension $n^4$.

**The quaternionic form.** For even $n$ there is a second real form $M_{n^2/2}(\mathbb{H})$, the fixed set of $X\mapsto C\bar XC^{-1}$ with $C$ a real matrix of size $n^2$ satisfying $C^2=-\mathrm I$. It is not the frame real form, and no change of frame makes the two equal, because they are non-isomorphic real algebras.

**The parity condition.** $M_{n^2/2}(\mathbb{H})$ needs $n^2$ even, that is $n$ even. At $n=2$ both forms exist, which is why the biquaternion series could use either; at $n=3$ only the split form exists.

## The Lie Algebra

**The real dimension.** $\mathfrak{gl}_{n^2}(\mathbb{C})$ has real dimension $2n^4$. Its traceless part has real dimension $2n^4-1$.

**The compact form.** $\mathfrak{u}(n^2)$, the skew-Hermitian matrices of the frame, has real dimension $n^4$ and is the compact real form. Its traceless part $\mathfrak{su}(n^2)$ has dimension $n^4-1$.

**The split form.** $\mathfrak{gl}_{n^2}(\mathbb{R})$ has the same real dimension $2n^4$ and is the split real form. The two are the extremes of the list of $\lfloor n^2/2\rfloor+1$ real forms of $\mathfrak{sl}_{n^2}$.

**The span inside.** The two-sided span $\mathfrak{a}=\operatorname{span}\{L_A,R_B\}$ has dimension $2n^2-1$ and is a real Lie algebra. Its compact form is $\mathfrak{u}(n)\oplus\mathfrak{u}(n)$ modulo the diagonal scalars, of dimension $2n^2-1$, and its split form is $\mathfrak{gl}_n(\mathbb{R})\oplus\mathfrak{gl}_n(\mathbb{R})$ modulo the diagonal.

*Proof.* The centraliser of $\mathfrak{a}$ in $\mathfrak{gl}_{n^2}$ is the scalars, so $\mathfrak{a}$ is reductive of dimension $2n^2-1$ with the two summands $\mathfrak{gl}_n$ intersecting in the scalars. $\square$

**The comparison of dimensions.** $2n^2-1$ against $n^4$: the compact form of the span is a tiny subalgebra of the compact form of the ambient algebra, of dimension $2n^2-1$ inside $n^4$.

## The Group

**The operator group.** The invertible operators on $M_n$ form $GL_{n^2}(\mathbb{C})$, of real dimension $2n^4$.

**The maximal compact.** $U(n^2)$ is the group of Hilbert–Schmidt isometries, of dimension $n^4$. It contains the operators $L_U$, $R_V$ and $T_{U,V}$ with $U,V$ unitary.

**The two-sided subgroup.** The pairs $(L_U,R_V)$ with $U,V\in U(n)$, modulo the diagonal scalars of order $n$, form a group of dimension $2n^2-1$, the compact group of the span. Its Lie algebra is the compact form above.

*Proof.* The map $(U,V)\mapsto(L_U,R_V)$ has kernel the diagonal pairs $(\zeta\mathrm I,\zeta^{-1}\mathrm I)$ with $\zeta^n=1$, of order $n$. $\square$

**The real forms of the group.** $GL_{n^2}(\mathbb{R})$ and, for even $n$, $GL_{n^2/2}(\mathbb{H})$, together with the unitary groups $U(p,q)$ with $p+q=n^2$. The maximal compact of every one of them is a conjugate of $U(n^2)$.

**The table.**

| $n$ | $2n^4$ | $n^4$ | $2n^2-1$ | real forms of the algebra |
|---|---|---|---|---|
| $2$ | $32$ | $16$ | $7$ | $M_4(\mathbb{R})$, $M_2(\mathbb{H})$ |
| $3$ | $162$ | $81$ | $17$ | $M_9(\mathbb{R})$ |
| $4$ | $512$ | $256$ | $31$ | $M_{16}(\mathbb{R})$, $M_8(\mathbb{H})$ |
| $5$ | $1250$ | $625$ | $49$ | $M_{25}(\mathbb{R})$ |

## What Does Not Generalise

**The four-dimensional accident.** At $n=2$ the operator space has real dimension $32$, the frame real form is $M_4(\mathbb{R})$, and the carrier of the biquaternion algebra is four real-dimensional. Every one of these numbers is small, and the biquaternion article could pass between them freely.

**The failure.** At $n\ge3$ the real form $M_{n^2}(\mathbb{R})$ is not the endomorphism algebra of a real $n^2$-dimensional space that also carries the carrier structure: the carrier $M_n$ has real dimension $2n^2$, and the split form acts on it only through the complex frame.

**The honest statement.** The real form of the algebra, the compact form of the Lie algebra and the maximal compact of the group are three different objects, with dimensions $n^4$, $n^4$ and $n^4$ in the first two cases and the span's $2n^2-1$ inside. The biquaternion series used one word for all of them.

## The Finite Check

The dimensions were computed for $n=2,3,4,5$: $2n^4$ gives $32,162,512,1250$; $n^4$ gives $16,81,256,625$; $2n^2-1$ gives $7,17,31,49$. The dimension of the span was confirmed by the rank of the linear system spanned by the $L_{E_{ij}}$ and $R_{E_{ij}}$, which is $2n^2-1$ in every case.

The real form was checked by counting the real parameters fixed by entrywise conjugation in the frame: $n^4$, that is $16,81,256,625$, matching $\dim_{\mathbb{R}}M_{n^2}(\mathbb{R})$. The quaternionic form was checked for $n=2$ and $n=4$ with $C$ the standard real matrix of $2\times2$ blocks $\begin{pmatrix}0&-1\\1&0\end{pmatrix}$: the fixed set of $X\mapsto C\bar XC^{-1}$ has real dimension $N^2$, that is $16$ and $256$, it is closed under multiplication, and it is not isomorphic to $M_{N}(\mathbb{R})$ because it contains no nonzero element whose square is $-\mathrm I$ commuting with everything. For $n=3,5$ no real $C$ with $C^2=-\mathrm I$ exists, since $N$ is odd.

## The Compact Real Form

**The Lie algebra.** The operator group of the Hilbert space is $U(N)$ with $N=n^2$, of real dimension $n^4$ and Lie algebra $\mathfrak{u}(N)$.

**The span, as a Lie algebra.** The left and right copies span a Lie subalgebra isomorphic to $\mathfrak{u}(n)\oplus\mathfrak{u}(n)$ modulo the diagonal scalars, of dimension $2n^2-1$; it is closed because $[L_K,R_H]=0$ and each copy is closed under the bracket.

**The table.**

| $n$ | $\dim\mathfrak{u}(n^2)=n^4$ | $\dim$ of the pair's span $=2n^2-1$ |
|---|---|---|
| $2$ | $16$ | $7$ |
| $3$ | $81$ | $17$ |
| $4$ | $256$ | $31$ |
| $5$ | $625$ | $49$ |

**The reading.** The pair's algebra is a small subalgebra of the compact form, and the gap $n^4-2n^2+1$ is the same gap that separates the bimodule operators from all operators.

**The integration.** The pair's algebra integrates to $(U(n)\times U(n))/U(1)$, the group of bimodule automorphisms up to scalars, and the full compact form integrates to $U(n^2)$, the group of all isometries of the operator space.

## The Two Reflections

**The adjoint reflection.** $T\mapsto T^{\dagger}$ is a real-linear involution of the operator space whose fixed set is the real vector space of self-adjoint operators, of dimension $n^4$.

**The transpose reflection.** $T\mapsto T^{\mathsf T}$ is a complex-linear involution with respect to the bilinear form; its fixed set is the space of symmetric operators, also of dimension $n^4(n^4+1)/2$ over $\mathbb{R}$.

**The table.**

| $n$ | $n^4$ self-adjoint | $n^4(n^4+1)/2$ symmetric |
|---|---|---|
| $2$ | $16$ | $136$ |
| $3$ | $81$ | $3321$ |
| $4$ | $256$ | $32896$ |

**The two reflections.** The first is antilinear-compatible (it is the real structure of the Hilbert space); the second is bilinear. They commute, and their composition is the conjugation $T\mapsto T^{*}$, which is the real structure used in the spin articles.

## The Real Forms of the Algebra

**The two forms.** The complex algebra $M_{n^2}(\mathbb{C})$ has two real forms up to isomorphism: $M_{n^2}(\mathbb{R})$ and, when $n^2$ is even, $M_{n^2/2}(\mathbb{H})$.

**The condition.** The quaternionic form exists exactly when $n^2$ is even, that is when $n$ is even, and it is the fixed set of a conjugation $X\mapsto C\bar XC^{-1}$ with $C^2=-\mathrm I$.

**The table.**

| $n$ | $n^2$ | real forms |
|---|---|---|
| $2$ | $4$ | $M_4(\mathbb{R})$, $M_2(\mathbb{H})$ |
| $3$ | $9$ | $M_9(\mathbb{R})$ |
| $4$ | $16$ | $M_{16}(\mathbb{R})$, $M_8(\mathbb{H})$ |
| $5$ | $25$ | $M_{25}(\mathbb{R})$ |

**The reading.** The parity of $n$ decides whether the operator space carries a quaternionic structure, and it decides it for the same reason as in the spin articles: the faithful copy needs an even number of dimensions to admit an anti-linear squaring to $-1$.

## The Count

**The numbers.** $n^{4}$ is $16,81,256,625$ and the subalgebra has dimension $7,17,31,49$ at $n=2,3,4,5$; the second is the first minus the gap $(n^{2}-1)^{2}$.

## Summary

The operator algebra has the real form $M_{n^2}(\mathbb{R})$ always and the quaternionic form only for even $n$. The Lie algebra has real dimension $2n^4$ and compact form $\mathfrak{u}(n^2)$ of dimension $n^4$. The group is $GL_{n^2}(\mathbb{C})$ with maximal compact $U(n^2)$. Inside, the span of the two one-sided families is a Lie algebra of dimension $2n^2-1$ with compact form $\mathfrak{u}(n)\oplus\mathfrak{u}(n)$ modulo scalars. At $n=2$ the numbers are small enough to be confused; at general $n$ they are not.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $N=n^2$ | the carrier dimension |
| $2n^4$ | the real dimension of the operator algebra |
| $\mathfrak{u}(n^2)$ | the compact real form, dimension $n^4$ |
| $2n^2-1$ | the dimension of the two-sided span |
| $M_{n^2/2}(\mathbb{H})$ | the quaternionic form, for even $n$ |

## Further Reading
- Onishchik and Vinberg, *Lie Groups and Algebraic Groups* (Springer, 1990), for real forms and compact forms.
- Helgason, *Differential Geometry, Lie Groups and Symmetric Spaces* (Academic Press, 1978), for the classification of real forms.
- [The Classification of the Structures of the Operators of $M_n(\mathbb{C})$](classification-of-the-structures-of-the-operators-of-mnc.html), for the five questions.
- [The Complex Structures of the Operators of $M_n(\mathbb{C})$, including Lie Algebras and Lie Groups](the-complex-structures-of-the-operators-of-mnc.html), for the complex side.
- [The Enveloping Operator Algebra of $M_n(\mathbb{C})$ and the Bi-module Structure](the-enveloping-operator-algebra-of-mnc.html), for the span and the centraliser.
- [The Spin Group via $4\times4$ Real Matrices](the-spin-group-via-4x4-real-matrices.html), for the case $n=2$.
