# __Introduction to the Carrier of Dimension 1 over C__

## Introduction

The biquaternion algebra $\mathbb{B}$ has one complex line that every unit of the algebra carries onto itself, and that line is the whole of the first case. The article does three things: it exhibits the line, it proves that no other line has the property, and it describes how the line sits against the idempotent constructions of the other two cases.

The problem the article answers is the first of three: how to obtain an invariant subspace of $\mathbb{B}$ of complex dimension $1$. The answer is not a construction but a computation of a fixed space, and the computation is one line.

The other two cases are *Introduction to the Carriers of Dimension 2 over C, where the subspace is built from a square root of the unit and a pair of idempotents, and *Introduction to the Carriers of Dimension 4 over $\mathbb{C}$, where the subspaces are the halves cut by the two involutions. The definitions are *The Carriers of the Biquaternion Algebra*; the eigenvalue reading is *The Weights of a Carrier*.

Nothing below is a statement of physics. The elements are written $X,Y$; the units are $e_t,\vec e_x,\vec e_y,\vec e_z$ with $e_t^2=e_t$ and $\vec e_k^{2}=-e_t$; the group of units of modulus one is $G=\mathrm{U}(2)$; and $*$ is the Hermitian conjugation.

## The Subspace

**Definition (the line).** The subspace of this article is

$$
\mathbb{B}_{C}=\mathbb{C}e_t,
$$

the centre of the algebra: the set of complex multiples of the unit.

It is a complex subspace of complex dimension $1$, of real dimension $2$, and it is spanned by $e_t$ alone.

## How the Line Is Obtained

**Proposition (it is the fixed space of the conjugation).** For every unit $u$ and every $\lambda\in\mathbb{C}$,

$$
u(\lambda e_t)u^{*}=\lambda e_t .
$$

*Proof.* $ue_tu^{*}=uu^{-1}e_t=e_t$ because $e_t$ is the unit of the algebra.

**Proposition (it is the kernel of the derived action).** For every $Y\in\mathbb{B}$,

$$
[Y,\lambda e_t]=0 .
$$

*Proof.* $\lambda e_t$ is central, so it commutes with $Y$.

**Theorem (no other line is fixed).** Let $W$ be a complex line on which $G$ acts trivially. Then $W=\mathbb{B}_{C}$.

*Proof.* Work in the model $\mathbb{B}\cong M_2(\mathbb{C})$ of *The $M_2(\mathbb{C})$ Pauli Representation*. A fixed element commutes with every unitary matrix. The unitary group spans $M_2(\mathbb{C})$ linearly, since $4=\dim_{\mathbb{C}}M_2(\mathbb{C})$ and the unitary matrices supply a basis; hence the commutant of $G$ in $M_2(\mathbb{C})$ is the commutant of $M_2(\mathbb{C})$, which is $\mathbb{C}\mathrm I_2$. The preimage of $\mathbb{C}\mathrm I_2$ under the isomorphism $\mathbb{B}\cong M_2(\mathbb{C})$ is $\mathbb{C}e_t$. A line of fixed vectors therefore lies in $\mathbb{C}e_t$ and, being a line, equals it.

**Theorem (no other line is invariant).** Let $W$ be a complex line with $uWu^{*}\subseteq W$ for every unit $u$. Then $W=\mathbb{B}_{C}$.

*Proof.* The conjugation is a group action by invertible linear maps, so $uWu^{*}\subseteq W$ with $\dim uWu^{*}=\dim W$ gives $uWu^{*}=W$. The line is therefore fixed as a subspace, and its elements are permuted among themselves; a group of linear maps preserving a one-dimensional space acts by scalars, so $u$ acts on $W$ by a character $\chi(u)\in\mathbb{C}^{\times}$. The character is continuous, so it is $u\mapsto\det(u)^{m}\lvert\det u\rvert^{2n}$ for integers $m,n$; the conjugate of $\chi$ is $\chi^{-1}$ because the conjugation is by an isometry, which forces $m=n=0$ and $\chi=1$. Hence $W$ consists of fixed vectors, and $W=\mathbb{B}_{C}$ by the previous theorem.

**Corollary (three ways, one line).** The centre, the fixed space of $G$, and the kernel of the derived action are the same subspace, and it is the only invariant complex line of $\mathbb{B}$.

## The Line Is Not a Peirce Corner

The idempotent construction of the dimension-two case produces four lines, and the centre is none of them.

**Theorem (the centre meets every corner in zero).** Let $e,f$ be a complete family, $e^2=e$, $f^2=f$, $ef=fe=0$, $e+f=e_t$, and let $\mathbb{B}_{st}=\{X:\tilde\Pi_sX\tilde\Pi_t=X\}$ be the four corners. Then

$$
\mathbb{B}_{st}\cap\mathbb{B}_{C}=0
$$

for every pair $(s,t)$.

*Proof.* Take $X=\lambda e_t\neq0$ in $\mathbb{B}_{st}$. Then $\lambda e_t=eXf$, so $\lambda e_t=e(\lambda e_t)f=\lambda\,ef=0$, a contradiction. The same computation at $\lambda=0$ gives only $0$.

**Corollary (what the line has not).** The line has no companion nilpotent, no decomposition into two coordinates, and no pair of opposite eigenvalues. Those belong to the corners and to the columns of the idempotent construction.

**Remark (the degenerate family).** The line is the diagonal corner of the one-element family $(e_t)$, whose complement is $0$. That family is not a pair of nonzero idempotents, and it has no mixed corners, so the Peirce decomposition it gives is the trivial one, $\mathbb{B}=\mathbb{B}_{++}$.

## The Eigenvalue Reading

Fix a unit real vector $\vec u$ and the Hermitian element $\tilde S(\vec u)=\tfrac12 i\vec u\cdot\vec e$ of *The Weights of a Carrier*.

**Proposition (the single eigenvalue).** On $\mathbb{B}_{C}$ the derivation by $\tilde S(\vec u)$ is zero, and the element itself acts by left multiplication as the scalar $\tfrac12 i\vec u\cdot\vec e$ evaluated on the line, that is by the scalar $0$ composed with the algebra product:

$$
\operatorname{ad}_{\tilde S(\vec u)}(e_t)=0,\qquad
\tilde S(\vec u)e_t=\tilde S(\vec u).
$$

*Proof.* The first is centrality. The second is the unit acting on the left; the right side is not a multiple of $e_t$, which is the reason the line is not preserved by left multiplication and the reason a carrier at this dimension needs the conjugation as its action.

**Remark (the action belongs to the subspace).** The line is invariant for the conjugation and not for left multiplication: $\tilde S(\vec u)e_t=\tilde S(\vec u)\notin\mathbb{C}e_t$ for $\vec u\neq0$. The same subspace is therefore reducible for one action and irreducible for the other, and the pair (subspace, action) is what the article is about.

## The Intersections with the Other Subspaces

| second subspace | intersection with $\mathbb{B}_{C}$ |
|---|---|
| a column $S_{\pm}(\vec u)$ | $0$ |
| a corner $\mathbb{B}_{st}$ | $0$ |
| $\mathbb{B}_{\Phi}$ | $0$ |
| $\mathbb{B}_{\Psi}$ | $\mathbb{B}_{C}$ |
| the real triple $\mathfrak{k}$ | $0$ |
| the imaginary triple $\mathfrak{p}$ | $0$ |

*Proof.* A column contains no central element, by the theorem on corners, since a column is a sum of two corners. $\mathbb{B}_{\Phi}$ consists of anti-Hermitian elements and $e_t$ is Hermitian and nonzero, so the intersection is zero; $ie_t$ is anti-Hermitian and lies in $\mathbb{B}_{\Phi}$, not in $\mathbb{B}_{C}$. $\mathbb{B}_{\Psi}$ consists of Hermitian elements and contains $e_t$, so it contains the line. The triples consist of pure quaternions, which have scalar part zero.

## Summary

The subspace of complex dimension $1$ is the centre $\mathbb{B}_{C}=\mathbb{C}e_t$. It is the fixed space of the conjugation, the kernel of the derived action, and the unique invariant complex line of the algebra. The uniqueness rests on the commutant of the unitary group being the scalars.

The line is not a Peirce corner: no corner contains a nonzero central element, so the idempotent construction of the dimension-two case does not produce it. Its single eigenvalue for the generator is $0$. It is invariant for the conjugation and not for left multiplication, which is why its action is the conjugation.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra, $M_2(\mathbb{C})$, complex dimension $4$ |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | the units, $e_t^2=e_t$ and $\vec e_k^{2}=-e_t$ |
| $\mathbb{B}_{C}=\mathbb{C}e_t$ | the centre, the invariant complex line |
| $G=\mathrm{U}(2)$ | the group of units of modulus one |
| $\operatorname{Ad}_u(X)=uXu^{*}$ | the conjugation by a unit |
| $\operatorname{ad}_Y(X)=[Y,X]$ | the derived action |
| $\mathbb{B}_{st}$ | the corners of an idempotent pair |
| $\mathbb{B}_{\Phi},\mathbb{B}_{\Psi}$ | the anti-Hermitian and Hermitian halves |
| $\mathfrak{k},\mathfrak{p}=i\mathfrak{k}$ | the real and imaginary pure quaternions |
| $\tilde S(\vec u)=\tfrac12 i\vec u\cdot\vec e$ | the Hermitian generator at a unit axis |

## Further Reading

- [The Carriers of the Biquaternion Algebra](the-carriers-of-the-biquaternion-algebra.html), for the definition of a subspace of this kind and the list of all of them.
- [The Weights of a Carrier](the-weights-of-a-carrier.html)
- [The Tensor Square of the Adjoint Module](the-tensor-square-of-the-adjoint-module.html), for the trivial summand and its dimension.
- [Introduction to the Peirce Basis over C](the-peirce-basis-over-c.html), for the idempotents, the four corners and the two summands.
- [Introduction to the Carriers of Dimension 4 over $\mathbb{C}$](the-carriers-of-dimension-4.html), for the four halves and the triples inside them.
- [Peirce Decompositions of the Biquaternion Algebra](the-peirce-decomposition-of-the-biquaternion-algebra.html), for the corners and the reason the centre lies in none of them.
- [Subspaces and Decompositions of the Biquaternion Algebra](subspaces-and-decompositions-of-the-biquaternion-algebra.html), for the centre among the six remarkable subspaces.
