# __The Adjoint of an Endomorphism__

## Introduction

A non-degenerate pairing on a linear space turns the endomorphism $A$ into a second endomorphism $A^{*}$, the adjoint, by moving $A$ from one side of the pairing to the other, and the article is about that operator: its existence and uniqueness, the description of its kernel and image as the paired complements of the image and kernel of $A$, the preservation of rank, invertibility and spectrum, the rule for the adjoint of a composite, and the identification of the adjoint with the transpose once a basis is fixed. The involution that the assignment $A \mapsto A^{*}$ defines on the endomorphism algebra is *Involutions of the Endomorphism Algebra*; the article here is its operator-level counterpart in the `*`-operator group, and it treats the adjoint as an operator rather than the involution as a structure.

The pairing, its non-degeneracy and the notion of a reflexive pairing are as in *Involutions of the Endomorphism Algebra*; the transpose of a linear map, its contravariance and the annihilator description of its kernel and image are *The Transpose of a Linear Map*; the dual involution is *Involutions of the Dual Space*. The passage from the pairing duality to the dual-space duality is *The Involution on the Dual Operator*; the group of endomorphisms with $A^{*}=A^{-1}$ is *Unitary Endomorphisms*; the forms themselves, their norms and the analysis they support are *Hilbert Algebras*, in Part II.

Throughout, $F$ is a field, $V$ is a finite-dimensional $F$-linear space, $E = \operatorname{End}_F(V)$, and $B$ is a non-degenerate reflexive pairing on $V$: bilinear with $B(y,x) = \varepsilon B(x,y)$ for a sign $\varepsilon$, or sesquilinear with respect to an involution $\varsigma$ of $F$. The adjoint of $A$ is $A^{*}$, defined by $B(Ax,y) = B(x,A^{*}y)$. No norm and no topology is used.

## The Adjoint Operator

**Theorem (existence, uniqueness, linearity).** For every $A \in E$ there is a unique endomorphism $A^{*} \in E$ with

$$
B(Ax,y) = B(x,A^{*}y) \qquad \text{for all } x,y \in V ,
$$

and the assignment $A \mapsto A^{*}$ is additive, of order two and anti-multiplicative: $(A^{*})^{*} = A$, $(A+B)^{*} = A^{*}+B^{*}$, $(AB)^{*} = B^{*}A^{*}$, and $(\lambda A)^{*} = \varsigma(\lambda)A^{*}$.

**Proof.** For fixed $y$ the map $x \mapsto B(Ax,y)$ is linear; since $z \mapsto B(\cdot,z)$ is a bijection $V \to V^{*}$ by non-degeneracy, there is a unique $A^{*}y$ representing it, and uniqueness in $y$ makes $A^{*}$ a map. Linearity of $A^{*}$ and the four laws follow by uniqueness exactly as in *Involutions of the Endomorphism Algebra*, which owns them.

**Definition.** An endomorphism is **self-adjoint** when $A^{*}=A$, **skew-adjoint** when $A^{*}=-A$, and **unitary** when $A^{*}A = AA^{*} = \mathrm{id}$.

## Kernel, Image and the Paired Complement

**Definition.** For a subspace $U \subseteq V$ the **paired complement** is

$$
U^{\mathrm{c}} = \{y \in V : B(x,y) = 0 \text{ for all } x \in U\} .
$$

**Proposition.** $U^{\mathrm{c}}$ is a subspace and $\dim_F U^{\mathrm{c}} = \dim_F V - \dim_F U$; moreover $(U^{\mathrm{c}})^{\mathrm{c}} = U$ when $B$ is reflexive, so the assignment $U \mapsto U^{\mathrm{c}}$ is an order-reversing bijection of the lattice of subspaces onto itself.

**Proof.** $U^{\mathrm{c}}$ is the kernel of the linear map $V \to U^{*}$, $y \mapsto B(\cdot,y)$, which is surjective because $B$ is non-degenerate; hence the dimension formula. Reflexivity gives $(U^{\mathrm{c}})^{\mathrm{c}} = U$, and both statements are the standard pairings of a form.

**Theorem (kernel and image of the adjoint).** For every $A \in E$,

$$
\ker A^{*} = (\operatorname{im}A)^{\mathrm{c}}, \qquad \operatorname{im}A^{*} = (\ker A)^{\mathrm{c}} , \qquad
\operatorname{rk}A^{*} = \operatorname{rk}A .
$$

**Proof.** $A^{*}y = 0$ means $B(x,A^{*}y) = 0$ for all $x$, that is $B(Ax,y) = 0$ for all $x$, which says $y \in (\operatorname{im}A)^{\mathrm{c}}$; this is the first identity. For the second, $A^{*}y$ ranges over the paired complement of $\ker A$: indeed $B(x,A^{*}y) = B(Ax,y)$ vanishes for all $y$ exactly when $x \in \ker A$, so $(\operatorname{im}A^{*})^{\mathrm{c}} = \ker A$, and taking paired complements gives the identity. The rank is unchanged because $\dim\ker A^{*} = \dim(\operatorname{im}A)^{\mathrm{c}} = \dim\ker A$.

**Corollary (invertibility and inverse).** $A$ is invertible if and only if $A^{*}$ is, and then $(A^{-1})^{*} = (A^{*})^{-1}$; the adjoint of the identity is the identity, and the adjoint of a scalar $\lambda$ is $\varsigma(\lambda)$.

**Proof.** $\operatorname{rk}A^{*} = \operatorname{rk}A$ makes invertibility correspond; from $AA^{-1}=\mathrm{id}$ and anti-multiplicativity, $(A^{-1})^{*}A^{*} = \mathrm{id}$, which is the inverse statement.

## Spectrum and the Matrix Form

**Proposition (spectrum).** $A^{*}$ has the same trace, the same determinant and the same characteristic polynomial as $A$; consequently the spectrum of $A^{*}$, with multiplicities, is the spectrum of $A$. In the bilinear case, if $\Phi$ is the Gram matrix of $B$ in a basis, then $[A^{*}] = \Phi^{-1}[A]^{\mathsf{T}}\Phi$, so $A^{*}$ is similar to the transpose of $A$.

**Proof.** $[A^{*}] = \Phi^{-1}[A]^{\mathsf{T}}\Phi$ is the matrix form of *Involutions of the Endomorphism Algebra*; a matrix and its transpose are similar over the semigroup generated by transposition, and they have the same characteristic polynomial, $\det(xI-A) = \det((xI-A)^{\mathsf{T}})$; conjugation by $\Phi$ preserves the characteristic polynomial. The trace and determinant are the coefficients of the characteristic polynomial in degrees $n-1$ and $0$.

**Example.** With the standard pairing $B(x,y) = \sum x_iy_i$ on $F^n$ the Gram matrix is the identity and $A^{*} = A^{\mathsf{T}}$; with $B(x,y) = x_1y_1 - x_2y_2$ on $F^2$ one has $A^{*} = \operatorname{diag}(1,-1)A^{\mathsf{T}}\operatorname{diag}(1,-1)$, which for $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ is $\begin{pmatrix} a & -c \\ -b & d \end{pmatrix}$: the diagonal entries are unchanged and the two off-diagonal entries change sign.

## The Adjoints of a Composite and the Involution

**Proposition (the adjoint of a composite).** For $A_1,\dots,A_k \in E$,

$$
(A_1A_2\cdots A_k)^{*} = A_k^{*}\cdots A_2^{*}A_1^{*} , \qquad
\Bigl(\sum_i A_i\Bigr)^{*} = \sum_i A_i^{*} .
$$

**Proof.** Induction on $k$ from $(AB)^{*}=B^{*}A^{*}$ and additivity.

**Remark (the involution on the endomorphism algebra).** The assignment $A \mapsto A^{*}$ is an involution of the algebra $E$ in the sense of *Involutive Rings*, of the first kind for a bilinear pairing and of the second kind for a sesquilinear one; its fixed and skew parts, its matrix description, the classification of the involutions it produces and the unitary elements are the subject of *Involutions of the Endomorphism Algebra*, and only the operator facts about a single adjoint are established here. The two articles divide the subject: that one treats the involution as a structure on the algebra, this one the adjoint as an operator on $V$.

**Remark (the involution and the operator adjoint).** There are two maps that the word "adjoint" names, and the article's symbol $\ast$ is the element involution on $E$ while the operator adjoint of a map on $E$ — the adjoint of $L_A$ for the natural pairing of the endomorphism algebra — is written ${}^{\dagger}$ and is *The Adjoint of the Left Multiplication on a Linear Space*.

## Summary

A non-degenerate reflexive pairing $B$ on a finite-dimensional space $V$ attaches to each endomorphism $A$ its adjoint $A^{*}$, uniquely determined by $B(Ax,y) = B(x,A^{*}y)$; the assignment is additive, of order two, anti-multiplicative and $\varsigma$-semilinear, so it is an involution of the endomorphism algebra, treated as a structure in *Involutions of the Endomorphism Algebra*. As an operator the adjoint is described by the paired complement: $\ker A^{*} = (\operatorname{im}A)^{\mathrm{c}}$, $\operatorname{im}A^{*} = (\ker A)^{\mathrm{c}}$, the paired complement being the order-reversing bijection $U \mapsto U^{\mathrm{c}}$ of the subspace lattice with $\dim U^{\mathrm{c}} = n - \dim U$. Consequently the rank is preserved, invertibility corresponds, and the inverse passes to the adjoint, $(A^{-1})^{*} = (A^{*})^{-1}$; the trace, determinant and characteristic polynomial are preserved, so the spectrum of $A^{*}$ is that of $A$, and in a basis $A^{*}$ is $\Phi^{-1}A^{\mathsf{T}}\Phi$. The adjoint of a product is the product of the adjoints in the reverse order. The dual-space duality and its compatibility with the pairing duality are *The Involution on the Dual Operator*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $F$, $\varsigma$ | the field and the involution of the sesquilinear case |
| $V$, $n$ | the space and its dimension |
| $E=\operatorname{End}_F(V)$ | the endomorphism algebra |
| $B$ | a non-degenerate reflexive pairing |
| $A^{*}$ | the adjoint, $B(Ax,y)=B(x,A^{*}y)$ |
| $U^{\mathrm{c}}$ | the paired complement, $\{y : B(x,y)=0 \ \forall x\in U\}$ |
| $\ker A^{*}=(\operatorname{im}A)^{\mathrm{c}}$ | the kernel of the adjoint |
| $\operatorname{im}A^{*}=(\ker A)^{\mathrm{c}}$ | the image of the adjoint |
| $\Phi$ | the Gram matrix; $[A^{*}]=\Phi^{-1}[A]^{\mathsf{T}}\Phi$ |
| $A^{*}=\pm A$ | self-adjoint and skew-adjoint |
| $A^{*}A=AA^{*}=\mathrm{id}$ | unitary |

## Further Reading

- Nicolas Bourbaki, *Algebra I: Chapters 1–3* (Springer, 1998), for sesquilinear pairings and adjoints.
- Werner Greub, *Linear Algebra* (Springer, 4th ed. 1975), for the adjoint of an endomorphism with respect to a bilinear pairing.
- Kenneth Hoffman and Ray Kunze, *Linear Algebra* (Prentice Hall, 2nd ed. 1971), for the adjoint, orthogonal complements and the spectrum.
- Serge Lang, *Linear Algebra* (Springer, 3rd ed. 1987), for duality, adjoints and the classical groups.
- Steven Roman, *Advanced Linear Algebra* (Springer, 3rd ed. 2008), for bilinear pairings, adjoints and their matrix descriptions.
