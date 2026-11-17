# __The Involutions of the First Kind: Transpose and Symplectic__

## Introduction

**Over $\mathbb{R}$ the involutions of the first kind fall into two types, the transpose and the symplectic, and their fixed spaces have the same dimension, $n(n+1)/2$, while one is a Jordan algebra and the other a Lie algebra.** The two types are told apart by a sign in the product rule, and the real base field adds what the complex field loses: the inertia of the form behind the involution, and with it the definiteness of the trace form on one fixed space and its indefiniteness on the other.

The article defines an involution of the first kind, proves that every such involution comes from a nondegenerate bilinear form, classifies the forms into the symmetric and the alternating case, computes the two fixed spaces, proves that one is a Jordan algebra and the other a Lie algebra, and states exactly what complexification does to the classification. It assumes *The Matrix Algebra $M_n(\mathbb{R})$* and *The Split Real Form: $M_n(\mathbb{R})$ inside $M_n(\mathbb{C})$*. It prepares *The Two Halves: Symmetric and Antisymmetric* and *The Two Classes Compared: $\operatorname{Sym}_n$ and $\mathfrak{sp}_n$ Have the Same Dimension*.

## The Definition

**An involution of the first kind is an $\mathbb{R}$-linear anti-automorphism of order two.** A map $\sigma:M_n(\mathbb{R})\to M_n(\mathbb{R})$ is such an involution when

$$
\sigma(X+Y)=\sigma(X)+\sigma(Y),\qquad \sigma(\lambda X)=\lambda\sigma(X),\qquad \sigma(XY)=\sigma(Y)\sigma(X),\qquad \sigma^{2}=\mathrm{id},
$$

for all $X,Y$ and all $\lambda\in\mathbb{R}$. The third condition is what makes it an anti-automorphism, and the second says that it fixes the base field: this is the meaning of **first kind**. An involution of the second kind would be conjugate linear, and over $\mathbb{R}$ the two notions coincide, which is why the real theory has one kind only.

**The transpose is the model.** $\sigma(X)=X^{\mathsf T}$ satisfies all four conditions, and its fixed space is $\operatorname{Sym}_n$.

**The fixed space and the anti-fixed space have dimensions that add to $n^{2}$.** Since $\sigma^{2}=\mathrm{id}$, the algebra is the direct sum

$$
M_n(\mathbb{R})=\{X:\sigma(X)=X\}\oplus\{X:\sigma(X)=-X\},
$$

of the $+1$ and $-1$ eigenspaces, and the projection onto the first is $\tfrac12(X+\sigma(X))$.

## The Form behind an Involution

**Every involution of the first kind is $\sigma_B(X)=B^{-1}X^{\mathsf T}B$ for a nondegenerate bilinear form $B$, and $B$ is unique up to a nonzero scalar.** A nondegenerate bilinear form is a matrix $B$ with $\det B\ne0$, and $\sigma_B$ is an anti-automorphism because $(XY)^{\mathsf T}=Y^{\mathsf T}X^{\mathsf T}$ and $B^{-1}$ cancels. The negative $-\sigma_B$ is also of order two and satisfies $\sigma(XY)=-\sigma(Y)\sigma(X)$; both signs occur, and the sign is the invariant that separates the two classes. The order-two condition is automatic: $\sigma_B^{2}(X)=X$. Conversely, an anti-automorphism of the matrix algebra is determined by its effect on the rank-one maps, which it permutes, and that permutation is induced by a linear map on the dual space; assembling the two gives $B$.

**The fixed space is the set of matrices self-adjoint for $B$.** The equation $\sigma_B(X)=X$ is $X^{\mathsf T}B=BX$, which says $\langle Xu,v\rangle=\langle u,Xv\rangle$ for the form $\langle u,v\rangle=u^{\mathsf T}Bv$. So the $+1$ space is the set of $B$-self-adjoint endomorphisms, and the $-1$ space is the set of $B$-anti-self-adjoint endomorphisms.

**Scaling the form does not change the involution.** $\sigma_{\lambda B}=\sigma_B$ for $\lambda\ne0$, because the two scalars cancel. So the data is the form up to a scalar, and the classification of involutions is the classification of forms up to similarity.

**The transpose is the case $B=\mathrm{I}$.** Then $\sigma_{\mathrm{I}}(X)=X^{\mathsf T}$ and the self-adjoint matrices are the symmetric ones.

## The Two Classes for Even $n$

**A nondegenerate form is either symmetric or alternating, and the two are not similar.** Over $\mathbb{R}$ a bilinear form decomposes into its symmetric part $\tfrac12(B+B^{\mathsf T})$ and its alternating part $\tfrac12(B-B^{\mathsf T})$, and the classification of forms by congruence splits accordingly. A form is **symmetric** when $B^{\mathsf T}=B$ and **alternating** when $B^{\mathsf T}=-B$; an alternating form satisfies $B(v,v)=0$ for every $v$, a symmetric one generally does not.

**The symmetric case gives the transpose class.** Every nondegenerate symmetric form is congruent to a diagonal form with entries $\pm1$, and the involution depends only on the similarity class. Taking $B=\mathrm{I}$ gives the transpose itself, so every symmetric case is conjugate to the transpose.

**The alternating case requires $n$ even and gives the symplectic class.** An alternating form has a basis in which

$$
B=J=\begin{pmatrix}0&1&&\\ -1&0&&\\&&\ddots&\\&&&0&1\\&&&-1&0\end{pmatrix},
$$

the block-diagonal matrix of $m=n/2$ copies of $\begin{pmatrix}0&1\\ -1&0\end{pmatrix}$. With this $B$,

$$
\sigma_B(X)=J^{-1}X^{\mathsf T}J=-JX^{\mathsf T}J,\qquad \sigma_J(X)=-JX^{\mathsf T}J^{-1}=JX^{\mathsf T}J,
$$

where the first is the anti-automorphism attached to $B=J$ and the second is its negative. The negative is the **symplectic involution** of this series: it is of order two and it satisfies the product rule with the minus sign.

**The two classes are not conjugate.** An alternating form is not similar to a symmetric one: $B^{\mathsf T}=B$ and $B^{\mathsf T}=-B$ together force $B=0$, which is excluded by nondegeneracy. Since conjugation of involutions corresponds to similarity of forms, the transpose and the symplectic involution are not conjugate, and their classes are the two of the title.

**Odd $n$ has one class only.** An alternating form exists only in even dimension, because an alternating matrix of odd size is singular. So for odd $n$ every involution of the first kind is conjugate to the transpose.

## The Fixed Spaces

**The fixed space of the transpose is $\operatorname{Sym}_n$, of dimension $n(n+1)/2$.** The equation $X^{\mathsf T}=X$ fixes the diagonal and the entries above it, so the free entries number $n+\binom{n}{2}$.

**The fixed space of the symplectic involution has the same dimension.** The equation $X=-JX^{\mathsf T}J^{-1}$ is equivalent to $(JX)^{\mathsf T}=JX$, so

$$
\{X:\sigma_J(X)=X\}=\{X: JX\in\operatorname{Sym}_n\}=J^{-1}\operatorname{Sym}_n,
$$

which is the image of $\operatorname{Sym}_n$ under the invertible map $S\mapsto J^{-1}S$. Hence the dimension is again $n(n+1)/2$. Measured by projecting the matrix units, the dimension is $3$, $10$, $21$ at $n=2,4,6$, which is $n(n+1)/2$ in each case.

**The two $-1$ spaces also have equal dimension, $n(n-1)/2$.** The anti-fixed space of the transpose is $\operatorname{Skew}_n$; the anti-fixed space of $\sigma_J$ is $\{X:JX\in\operatorname{Skew}_n\}=J^{-1}\operatorname{Skew}_n$. So the dimension count does not separate the two classes at all: only the algebraic nature of the fixed space does.

**The two involutions are distinguished by the trace form on their fixed spaces.** On $\operatorname{Sym}_n$ the form $\operatorname{tr}(XY)$ is positive definite and on $\operatorname{Skew}_n$ negative definite. On $\mathfrak{sp}_n$ the same form is indefinite: computed on a basis of $\mathfrak{sp}_n$ it has inertia $(2,1)$, $(6,4)$, $(12,9)$ at $n=2,4,6$. So the restriction of the trace form separates the two classes, while the dimension does not.

## One Jordan Algebra and One Lie Algebra

**$\operatorname{Sym}_n$ is a Jordan algebra.** It is closed under the anticommutator

$$
X\circ Y=\tfrac12(XY+YX),
$$

because $(XY+YX)^{\mathsf T}=Y^{\mathsf T}X^{\mathsf T}+X^{\mathsf T}Y^{\mathsf T}=YX+XY$, and the product is commutative and satisfies the Jordan identity. It is not closed under the commutator: the bracket of two symmetric matrices is antisymmetric and generally nonzero.

**The fixed space of $\sigma_J$ is a Lie algebra.** It is $\mathfrak{sp}_n$, the symplectic Lie algebra, closed under the commutator. In symbols, if $JX$ and $JY$ are symmetric then

$$
J[X,Y]=JXY-JYX,
$$

and transposing uses the symmetry of $JX$ and $JY$ to show that $J[X,Y]$ is symmetric again. On $100$ random pairs of elements of the fixed space the commutator stays in the space in every case; on $100$ random pairs of symmetric matrices the commutator is symmetric in no case.

**The mechanism is a sign in the product rule.** The transpose satisfies $\sigma(XY)=\sigma(Y)\sigma(X)$. The map $\sigma_J$ satisfies

$$
\sigma_J(XY)=-\sigma_J(Y)\sigma_J(X),
$$

because $(XY)^{\mathsf T}=Y^{\mathsf T}X^{\mathsf T}$ and the two factors $-J$ and $J^{-1}$ combine to $-1$ after the reversal. So $\sigma_J$ reverses the product up to a sign. For $X,Y$ fixed by $\sigma_J$,

$$
\sigma_J([X,Y])=[X,Y],\qquad \sigma_J(XY+YX)=-(XY+YX),
$$

so the fixed space is closed under the commutator and the anti-fixed space under the anticommutator. Measured on $100$ random pairs of fixed elements, the commutator stays fixed in every case; for the transpose the roles are exchanged, and on $100$ random pairs of symmetric matrices the commutator is symmetric in no case.

**The two involutions are mirror images.** The transpose gives a Jordan algebra $\operatorname{Sym}_n$ of dimension $n(n+1)/2$ and a Lie algebra $\operatorname{Skew}_n$ of dimension $n(n-1)/2$; $\sigma_J$ gives a Lie algebra $\mathfrak{sp}_n$ of dimension $n(n+1)/2$ and an anti-fixed space of dimension $n(n-1)/2$ closed under the anticommutator. The dimensions are exchanged along with the algebraic nature, which is the comparison of *The Two Classes Compared: $\operatorname{Sym}_n$ and $\mathfrak{sp}_n$ Have the Same Dimension*.

**The bracket of two anti-fixed elements lands in the fixed space.** For $X,Y$ anti-fixed by $\sigma_J$ one computes $\sigma_J([X,Y])=[X,Y]$ and $\sigma_J(XY+YX)=-(XY+YX)$, so $[\mathfrak{p},\mathfrak{p}]\subseteq\mathfrak{sp}_n$. This is the pattern of a symmetric pair: the anti-fixed space is the complement $\mathfrak{p}$ and the fixed space is the Lie algebra $\mathfrak{k}$. *Symmetric Pairs and Cartan Pairs: the Reductivity Criterion over $\mathbb{R}$* develops the criterion in this form.

## What the Base Field Changes

**Complexification keeps the two types.** The formulas $\sigma_B(X)=B^{-1}X^{\mathsf T}B$ and $\sigma_J(X)=-JX^{\mathsf T}J^{-1}$ make sense over any field, and conjugation by an invertible matrix preserves the sign in the product rule. The transpose has the sign $+$ and $\sigma_J$ the sign $-$, so the two are not conjugate over $\mathbb{C}$ either: the sign is an invariant of the conjugacy class.

**What complexification collapses is the inertia.** Over $\mathbb{C}$ a nondegenerate symmetric form is determined up to congruence by its rank, so every orthogonal involution is conjugate to the transpose. Over $\mathbb{R}$ Sylvester's law gives the inertia $(p,q)$ with $p+q=n$, and

$$
\sigma_{\operatorname{diag}(\mathrm{I}_p,-\mathrm{I}_q)}(X)=\operatorname{diag}(\mathrm{I}_p,-\mathrm{I}_q)\,X^{\mathsf T}\operatorname{diag}(\mathrm{I}_p,-\mathrm{I}_q)
$$

is conjugate to the transpose only when $p=n$ or $q=n$. So the transpose type is a single class over $\mathbb{C}$ and an inertia's worth of classes over $\mathbb{R}$, and this refinement is a real phenomenon that disappears on complexification.

**Definiteness exists only over $\mathbb{R}$.** The form $\operatorname{tr}(XY)$ is positive definite on $\operatorname{Sym}_n$ over $\mathbb{R}$ because it is a sum of squares, and that statement has no meaning over $\mathbb{C}$, where no nonzero vector has a sign. So the definite fixed space of the transpose, and the indefinite fixed space of $\sigma_J$, are visible only in the real category.

## Summary

An involution of the first kind is an $\mathbb{R}$-linear anti-automorphism of order two, and every such involution is $\sigma_B(X)=B^{-1}X^{\mathsf T}B$ for a nondegenerate form $B$ unique up to a scalar. Symmetric forms give the transpose type, alternating forms the symplectic type $\sigma_J(X)=-JX^{\mathsf T}J^{-1}$, which needs even $n$. Both fixed spaces have dimension $n(n+1)/2$; $\operatorname{Sym}_n$ is a Jordan algebra and $\mathfrak{sp}_n$ is a Lie algebra, and both $-1$ spaces have dimension $n(n-1)/2$. The trace form is definite on $\operatorname{Sym}_n$ and indefinite on $\mathfrak{sp}_n$, with inertias $(2,1)$, $(6,4)$, $(12,9)$ at $n=2,4,6$. Over $\mathbb{C}$ the two types remain but each is a single class, because the inertia of a symmetric form is no longer an invariant.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\sigma$ | an involution of the first kind, an anti-automorphism of order two |
| $\sigma_B(X)=B^{-1}X^{\mathsf T}B$ | the involution attached to the nondegenerate form $B$ |
| $J$ | the standard alternating matrix, $J^{2}=-\mathrm{I}$ |
| $\sigma_J(X)=-JX^{\mathsf T}J^{-1}$ | the symplectic involution |
| $\operatorname{Sym}_n$ | the fixed space of the transpose, a Jordan algebra |
| $\mathfrak{sp}_n$ | the fixed space of $\sigma_J$, a Lie algebra |

## Further Reading

- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for involutions of the first and second kind and their classification by forms.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for self-adjoint and anti-self-adjoint endomorphisms of a bilinear form.
- [The Matrix Algebra $M_n(\mathbb{R})$](the-matrix-algebra-mnr.html), for the transpose and the two halves.
- [Split-Quaternion Algebra](split-quaternion-algebra.html), for the one-dimensional case of the classification.
- [The Matrix Algebra $M_n(\mathbb{C})$](the-matrix-algebra-mnc.html), for the complex algebra where one class remains.
