# __The Classification of the Structures of the Operators of $M_n(\mathbb{C})$__

## Introduction

**The question.** Which structures can be put on the operator space $\operatorname{End}(M_n(\mathbb{C}))$, and how many of each are there?

**The answer in one line.** The answer depends on which structure is asked for, and the counts are wildly different: one complex structure on the algebra, one or two real forms of it, $\lfloor n^2/2\rfloor+1$ real forms of its Lie algebra, and $2n^8$ complex structures on the underlying real space.

**Why the article is needed.** The biquaternion series could speak of "the real structure" because at $n=2$ the operator space is $M_4(\mathbb{C})$ and every count collapses to a small number. At general $n$ the same words name different classification problems, and a reader who mixes them will compare a count of two with a count of nine. This article fixes the questions before the two lists answer them.

**Boundaries.** The real answers are *The Real Structures of the Operators of $M_n(\mathbb{C})$, including Lie Algebras and Lie Groups*; the complex answers are *The Complex Structures of the Operators of $M_n(\mathbb{C})$, including Lie Algebras and Lie Groups*; the algebra itself is *The Matrix Algebra $M_n(\mathbb{C})$*.

**Conventions.** $N=n^2$ is the dimension of the carrier of operators, so $\operatorname{End}(M_n)\cong M_N(\mathbb{C})$ has complex dimension $N^2=n^4$ and real dimension $2N^2=2n^4$. A real form of a complex object is a real object whose complexification is the given one. An antilinear involution is a conjugate-linear map $J$ with $J^2=\pm1$.

## The Questions

**Q1, the algebra.** Real forms of the associative algebra $M_N(\mathbb{C})$: real algebras $A$ with $A\otimes_{\mathbb{R}}\mathbb{C}\cong M_N(\mathbb{C})$.

**Q2, the Lie algebra.** Real forms of $\mathfrak{gl}_N(\mathbb{C})$ and of $\mathfrak{sl}_N(\mathbb{C})$: real Lie algebras $\mathfrak{g}$ with $\mathfrak{g}\otimes\mathbb{C}\cong\mathfrak{gl}_N(\mathbb{C})$.

**Q3, the group.** Real forms of $GL_N(\mathbb{C})$: real Lie groups whose complexification is $GL_N(\mathbb{C})$.

**Q4, the vector space.** Complex structures on the real vector space $\mathbb{R}^{2N^2}$: real linear maps $J$ with $J^2=-\mathrm I$.

**Q5, the involutions.** Antilinear involutions of $M_N(\mathbb{C})$: the conjugations $X\mapsto SX^{*}S^{-1}$ and $X\mapsto SX^{\mathsf T}S^{-1}$ and their relatives, up to conjugacy.

**The point.** Q1, Q2, Q5 are three different classifications of three different objects. Q1 asks for subalgebras, Q2 for Lie subalgebras, Q5 for fixed sets of conjugations. The fixed set of a conjugation need not be a subalgebra, and that single fact separates the answers.

## The Associative Answer

**Theorem.** $M_N(\mathbb{C})$ has exactly one real form when $N$ is odd, and exactly two when $N$ is even: $M_N(\mathbb{R})$ always, and $M_{N/2}(\mathbb{H})$ when $N$ is even.

*Proof (sketch).* Let $A$ be a real form. Then $A$ is a real central simple algebra of real dimension $N^2$. By Wedderburn every real central simple algebra is $M_k(\mathbb{R})$, $M_k(\mathbb{C})$ or $M_k(\mathbb{H})$, with real dimensions $k^2$, $2k^2$ and $4k^2$. Setting the dimension equal to $N^2$ leaves $k=N$ in the first case, no solution in the second, and $k=N/2$ in the third, which requires $N$ even. $\square$

**The count for the operators.** With $N=n^2$: one real form when $n$ is odd, two when $n$ is even. The split is $M_{n^2}(\mathbb{R})$ always, and $M_{n^2/2}(\mathbb{H})$ for even $n$.

**The fixed sets.** Each real form is the fixed set of an antilinear involution of $M_N$: $X\mapsto\bar X$ for $M_N(\mathbb{R})$, and $X\mapsto J\bar XJ^{-1}$ for $M_{N/2}(\mathbb{H})$ with $J$ a quaternionic structure.

**The warning.** The real forms of the algebra are few. The real forms of the Lie algebra are many. The reason is Q1 against Q2: the pseudo-Hermitian fixed sets $\{X:IX^{*}I=X\}$ for indefinite $I$ are closed under the commutator but not under the product.

## The Lie Answer

**Theorem.** The real forms of $\mathfrak{sl}_N(\mathbb{C})$ are $\mathfrak{sl}_N(\mathbb{R})$ and $\mathfrak{su}(p,q)$ with $p+q=N$, up to $\mathfrak{su}(p,q)\cong\mathfrak{su}(q,p)$.

**The count.** $\lfloor N/2\rfloor+1$ real forms. For the operators, $N=n^2$:
$$
\lfloor n^2/2\rfloor+1 .
$$

**The table.**

| $n$ | $N=n^2$ | real forms of $\mathfrak{sl}_N$ |
|---|---|---|
| $2$ | $4$ | $3$ |
| $3$ | $9$ | $5$ |
| $4$ | $16$ | $9$ |
| $5$ | $25$ | $13$ |

**The compact form.** $\mathfrak{su}(N)$ is the compact real form, of real dimension $N^2-1$, and it is the one the Hilbert–Schmidt metric singles out. The real form $\mathfrak{sl}_N(\mathbb{R})$ is split, of the same dimension, and the two are the extremes of the list.

**The operator reading.** $\operatorname{End}(M_n)$ as a Lie algebra is $\mathfrak{gl}_{n^2}$, so the operator group has $\lfloor n^2/2\rfloor+1$ real forms of its traceless part. The compact one is $\mathfrak{su}(n^2)$, the isometries of the Hilbert–Schmidt space.

## The Vector-Space Answer

**Theorem.** The set of complex structures on $\mathbb{R}^{2N^2}$ is $GL_{2N^2}(\mathbb{R})/GL_{N^2}(\mathbb{C})$, of real dimension $2N^4=2n^8$.

*Proof.* $GL_{2m}(\mathbb{R})$ acts transitively on complex structures on $\mathbb{R}^{2m}$, and the stabiliser of the standard one is $GL_m(\mathbb{C})$. The dimension is $4m^2-2m^2=2m^2$ with $m=N^2=n^4$. $\square$

**The metric-compatible subclass.** Complex structures that are orthogonal for the Hilbert–Schmidt metric form $O(2m)/U(m)$, of real dimension $m(m-1)=n^4(n^4-1)$.

**The algebra-compatible subclass.** Complex structures that are algebra automorphisms are the elements $J$ of the centre with $J^2=-\mathrm I$. The centre is $\mathbb{C}$, so $J=\pm i$: one point, up to conjugacy none at all.

**The three numbers.** $2n^8$ for all, $n^4(n^4-1)$ for the orthogonal ones, $0$ for the algebra ones. The same word "complex structure" gives three different answers depending on what must be preserved, and this is the reason this article precedes the two lists.

## The Involution Answer

**The transposition.** $X\mapsto X^{\mathsf T}$ is a complex-linear involution of the algebra, not an antilinear one. Its fixed space is the symmetric matrices, of dimension $N(N+1)/2$, and the anti-fixed space is the antisymmetric matrices.

**The adjoint.** $X\mapsto X^{*}$ is antilinear and involutive, with fixed space the Hermitian matrices, a real space of dimension $N^2$.

**The product.** $X\mapsto X^{\mathsf T}$ composed with $X\mapsto X^{*}$ is the entrywise conjugation $X\mapsto\bar X$, whose fixed space is $M_N(\mathbb{R})$.

**The classification of the three.** The transposition is complex-linear and needs no metric; the adjoint is antilinear and depends on the positive definite form, and all choices are conjugate under the unitary group; the entrywise conjugation is the antilinear involution whose fixed set is the real form $M_N(\mathbb{R})$ of Q1.

## The Finite Check

The dimension counts were computed for $n=2,3,4,5$: $N=n^2$ gives $N^2=n^4$, the real dimension $2n^4$, the complex-structure dimension $2n^8$, the orthogonal complex-structure dimension $n^4(n^4-1)$, and the Lie-form count $\lfloor n^2/2\rfloor+1$. The values are $2n^8=512,13122,131072,781250$ and $n^4(n^4-1)=240,6480,65280,390000$.

The transposition and adjoint fixed-space dimensions were checked by counting the real parameters of the equations $X=X^{\mathsf T}$, $X=X^{*}$ and $X=\bar X$: $N(N+1)/2$, $N^2$ and $N^2$ in real terms, that is $10,45,136,325$ for the symmetric and $16,81,256,625$ for the Hermitian at $n=2,3,4,5$.

## The Five Questions

| question | real answer | complex answer |
|---|---|---|
| inner product | symmetric, definite | Hermitian, definite |
| complex structure | $2n^8$ of them | one central, $2n^8$ linear |
| real form | $n^4+(n^4-1)$ reflections | the conjugation $\Theta$ |
| transpose | one bilinear form, many symmetry groups | the flip |
| Lie algebra | $\mathfrak{u}(n^2)$ and its real forms | $\mathfrak{gl}(n^2,\mathbb{C})$ |

**The reading.** The real column asks how many structures exist; the complex column asks which structure is canonical. The two columns answer different questions, and the tables in the next two articles are the two columns in full.

**The consequence.** A sentence of the form "the operator space has a complex structure" is a complex-column sentence: the structure is canonical. A sentence of the form "the operator space has $2n^8$ complex structures" is a real-column sentence: the structures form a moduli space. The two must not be mixed.

**The order of the questions.** The first and fourth are bilinear-form questions; the second and third are real-form questions; the fifth is a Lie-theoretic question that uses the first four.

## What Is Not Asked

**Not asked: a classification up to isomorphism.** All the structures of one kind form a single orbit under the relevant group, so the classification up to isomorphism is trivial and the content is in the dimension of the orbit space.

**Not asked: the exceptional structures.** There is no exceptional complex structure, no exceptional real form, and no exceptional inner product: the operator space is a Hilbert space, and its structures are the standard ones.

**Not asked: the algebra structures.** A multiplication on the operator space making it an algebra is a different question, answered by the classification of the algebra structures on $M_{n^2}$, and it is not part of this series.

**The reading.** The five questions are the five structures that the operator space carries because it is an endomorphism algebra of a Hilbert space. Anything else is a structure of the algebra $M_{n^2}$, not of the space.

## The Answer in One Table

| structure | the canonical one | the moduli |
|---|---|---|
| inner product | Hilbert–Schmidt | a point up to $U(N)$ |
| complex structure | multiplication by $i$ | $2n^8$ of them |
| real form | entrywise conjugation | $n^4+(n^4-1)$ reflections |
| transpose | the flip | the symmetry group of the two-sided family |
| Lie algebra | $\mathfrak{u}(n^2)$ | its real forms |

**The reading.** Each row has a canonical object and a moduli space, and the articles that follow fill one row each.

## Summary

There are five different classification questions, and their answers are one or two (real forms of the algebra), $\lfloor n^2/2\rfloor+1$ (real forms of the Lie algebra), $2n^8$ (complex structures on the real space), $n^4(n^4-1)$ (orthogonal complex structures) and one (complex structures on the algebra). The associative and the Lie answers differ because the fixed set of an indefinite conjugation is not closed under multiplication. The next two articles give the real and the complex lists in full.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $N=n^2$ | the carrier dimension |
| $\lfloor n^2/2\rfloor+1$ | the number of real forms of $\mathfrak{sl}_{n^2}$ |
| $2n^8$ | the dimension of the space of complex structures |
| $n^4(n^4-1)$ | the dimension of the orthogonal ones |
| $M_{n^2/2}(\mathbb{H})$ | the quaternionic real form, for even $n$ |

## Further Reading
- Weil, *Basic Number Theory* (Springer, 1967), for central simple algebras and their forms.
- Onishchik and Vinberg, *Lie Groups and Algebraic Groups* (Springer, 1990), for the real forms of $\mathfrak{sl}_N$.
- [The Real Structures of the Operators of $M_n(\mathbb{C})$, including Lie Algebras and Lie Groups](the-real-structures-of-the-operators-of-mnc.html), for the real list.
- [The Complex Structures of the Operators of $M_n(\mathbb{C})$, including Lie Algebras and Lie Groups](the-complex-structures-of-the-operators-of-mnc.html), for the complex list.
- [The Matrix Algebra $M_n(\mathbb{C})$](the-matrix-algebra-mnc.html), for the algebra.
- [The Ideals, the Centre and the Simplicity of $M_n(\mathbb{C})$](the-ideals-the-centre-and-the-simplicity-of-mnc.html), for the centre that fixes the complex structure.
