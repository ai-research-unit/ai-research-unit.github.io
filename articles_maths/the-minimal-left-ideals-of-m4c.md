# __The Minimal Left Ideals of $M_4(\mathbb{C})$ and the Module $V_{3/2}$__

## Introduction

**The subject.** A minimal left ideal of the matrix algebra is a left ideal of dimension four, and every such ideal is isomorphic, as a module of the principal copy, to the module $V_{3/2}$. The ideal is therefore the place inside the algebra where the half-integer label lives, and the article proves this in three steps: the dimension, the weights, and the isomorphism.

**The order of the article.** The first section builds the ideals from rank-one idempotents and proves that they have dimension four. The second computes the weights of the left multiplication on an ideal and finds them to be the weights of the module. The third proves the isomorphism. The fourth exhibits the exterior cube as a second model. The fifth states the boundary with the conjugation decomposition.

**It assumes** *The Matrix Algebra $M_4(\mathbb{C})$* and the article on the principal copy, *The Spin Group at $n=4$: the Principal Copy, $\operatorname{Sym}^3$ and the Kernel $\{\pm\mathrm I\}$*, for the generators. The row at order two is *The Minimal Left Ideals of the Biquaternion Algebra*.

**The result in one line.** $M_4P\cong V_{3/2}$ for every rank-one idempotent $P$, with the weights $\tfrac32,\tfrac12,-\tfrac12,-\tfrac32$ supplied by the left multiplication; hence the label $\tfrac32$ occurs in the algebra, but only on the one-sided side.

**Boundaries.** The article does not treat the two-sided objects; they are *The Two-Sided Operators and the Segre Cone at $n=4$*. It does not treat the exterior cube except for one proposition; that is *The Exterior Cube Isomorphism $\Lambda^3V\cong V$ and $M_4(\mathbb{C})$ as $V\otimes V$*.

## The Ideals from Idempotents

**Definition.** An element $P\in M_4(\mathbb{C})$ is a **rank-one idempotent** when $P^{2}=P$ and $\operatorname{rank}P=1$. The **left ideal** attached to it is $M_4P=\{XP:X\in M_4(\mathbb{C})\}$.

**Proposition.** $M_4P$ is a left ideal of dimension four, and it is minimal: it contains no nonzero left ideal smaller than itself.

*Proof.* For $A\in M_4$ and $XP\in M_4P$ one has $A(XP)=(AX)P\in M_4P$, so it is a left ideal. The map $X\mapsto XP$ has kernel the matrices vanishing on the image of $P$, of dimension twelve, so the image has dimension $16-12=4$. For minimality, let $J\subsetneq M_4P$ be a nonzero left ideal and pick $0\neq Y\in J$; since $Y=YP$, the matrix $Y$ has rank one and the same image as $P$, so $M_4Y=M_4P$ and $J=M_4P$.

**Corollary.** $M_4P=\{X:\operatorname{im}X\subseteq\operatorname{im}P\}$.

*Proof.* $XP$ has image inside the image of $P$, and conversely a matrix whose image lies in the line of $P$ and which annihilates the kernel of $P$ is fixed by $P$ on the right.

**Corollary.** $M_4P$ depends only on the image of $P$, and the map $P\mapsto M_4P$ from rank-one idempotents to minimal left ideals is onto and has fibres of dimension three.

*Proof.* The first claim is the previous corollary. For the fibre, the idempotents with image the line $\mathbb{C}v$ are the maps $P=vw^{\mathsf T}$ with $w^{\mathsf T}v=1$, an affine hyperplane of the dual space, of dimension three.

**Corollary.** The minimal left ideals are parametrised by the lines of $\mathbb{C}^4$, that is, by $\mathbb{P}^3$.

*Proof.* Each ideal is $M_4P$ for the line $\operatorname{im}P$, and distinct lines give distinct ideals, since the two ideals contain matrices with different images.

## The Weights on an Ideal

**Definition.** Let $J_z$ be the diagonal generator of the copy in the weight basis, and let $L_{J_z}$ be the left multiplication $X\mapsto J_zX$.

**Proposition.** With $P$ the idempotent of image the first coordinate line, $M_4P$ has the basis $E_{00},E_{10},E_{20},E_{30}$ and $L_{J_z}$ acts on $E_{i0}$ by the eigenvalue $m_i$, where $m_0,m_1,m_2,m_3$ are $\tfrac32,\tfrac12,-\tfrac12,-\tfrac32$.

*Proof.* $E_{i0}$ has a single nonzero entry, in row $i$ and column $0$. Left multiplication by the diagonal matrix $J_z$ multiplies that row by the diagonal entry $m_i$, so $J_zE_{i0}=m_iE_{i0}$.

**Corollary.** The weights of $L_{J_z}$ on $M_4P$ are $\tfrac32,\tfrac12,-\tfrac12,-\tfrac32$, each once.

*Proof.* The four basis vectors have the four distinct eigenvalues displayed.

**The contrast with the adjoint action.** On the whole algebra the adjoint action of $J_z$, $X\mapsto J_zX-XJ_z$, has the integer eigenvalues $m_i-m_j$, because a matrix element in row $i$ and column $j$ is multiplied by $m_i-m_j$. On the ideal the action is one-sided, only the row index contributes, and the eigenvalues are half-integers.

*Proof.* $(J_zX-XJ_z)_{ij}=(m_i-m_j)X_{ij}$, while $(J_zX)_{ij}=m_iX_{ij}$.

**Corollary.** The adjoint weights on the algebra are all integers, so the half-integer weights of the ideal belong to the one-sided action only.

*Proof.* The adjoint eigenvalues are differences of half-integers.

## The Isomorphism with the Module

**Proposition.** $M_4P$ is irreducible as a module of the copy under left multiplication.

*Proof.* A submodule is the sum of the weight lines it contains. The lowering operator $L_{J_-}$ sends $E_{00}$ to $\sqrt3E_{10}$, then $E_{10}$ to $2E_{20}$, then $E_{20}$ to $\sqrt3E_{30}$, and kills $E_{30}$; the coefficients are the same as in the module. A submodule containing the top weight contains all four, and a nonzero submodule not containing the top weight is not stable under $L_{J_+}$, since $L_{J_+}$ raises the weight.

**Theorem.** $M_4P\cong V_{3/2}$ as modules of the copy, for every rank-one idempotent $P$.

*Proof.* Both spaces are irreducible, of dimension four, and have a vector of weight $\tfrac32$: $E_{00}$ in the ideal and $u^3$ in the module. An irreducible module of highest weight $j$ is determined up to isomorphism by $j$, so the two are isomorphic; the isomorphism sends $E_{k0}$ to the weight vector of weight $m_k$.

**Corollary.** The label of every minimal left ideal is $\tfrac32$, and it is the same for all of them, although the ideals themselves are distinct subspaces.

*Proof.* The theorem applies to every $P$, and the ideals for different lines are different subspaces of the algebra even though they are isomorphic as modules.

**Corollary.** The dimension count agrees: $4=2\cdot\tfrac32+1$ on both sides.

*Proof.* The highest weight is $\tfrac32$ and the dimension is four.

## The Exterior Cube as a Second Model

**Proposition.** The exterior cube $\Lambda^3V$ has dimension four, and its weights are the weights of $V$.

*Proof.* A basis of $\Lambda^3V$ is given by the four triples of distinct weights, that is, by omitting one weight from the set $\{\tfrac32,\tfrac12,-\tfrac12,-\tfrac32\}$. The weight of such a triple is the sum of its three members, which equals minus the omitted weight, since the total of the four weights is zero. The multiset of weights of the cube is therefore the same as that of $V$.

**Corollary.** $\Lambda^3V\cong V$ as modules, and the highest weight vector of the cube is the triple omitting the lowest weight.

*Proof.* Same dimension, same multiset of weights with multiplicity one, and the highest weight $\tfrac32$ occurs.

**Corollary.** The dual of $V$ is isomorphic to $V$, and the exterior cube realises the duality together with the invariant alternating form of order four.

*Proof.* The pairing $\Lambda^3V\otimes V\to\Lambda^4V\cong\mathbb{C}$ is perfect, so $\Lambda^3V\cong V^{*}$; the module is self-dual through its invariant Hermitian form, so $V^{*}\cong V$.

## The Boundary

**Against the summands.** The conjugation decomposition of the algebra is the sum of $V_3,V_2,V_1,V_0$, of dimensions $7,5,3,1$, and every label is an integer. The ideal $M_4P$ has label $\tfrac32$ and is not one of the summands; it is not even stable under conjugation, since conjugation carries it to another ideal, as the article on the missing label proves.

**Against the two-sided operators.** The two-sided operators act on the algebra and their rank layer is computed elsewhere; the left ideal is a subspace of the algebra and not an operator on it. The two objects are different in kind: one is a space of states, the other is a map.

**Against the module.** The module $V_{3/2}$ is the abstract carrier; the ideal is a concrete copy of it inside the algebra. The copy exists for each line of $\mathbb{C}^4$, so the algebra contains a $\mathbb{P}^3$-family of copies of its own spin module.

## Summary

A rank-one idempotent $P$ produces a minimal left ideal $M_4P$ of dimension four. The left multiplication by the diagonal generator has the eigenvalues $\tfrac32,\tfrac12,-\tfrac12,-\tfrac32$ on the basis $E_{00},E_{10},E_{20},E_{30}$, so the ideal carries the weights of the module and is isomorphic to $V_{3/2}$.

The ideals depend only on the image of the idempotent and are therefore parametrised by the lines of $\mathbb{C}^4$, that is, by $\mathbb{P}^3$; the idempotents themselves form a three-dimensional affine space over each line. The exterior cube is a second model of the same module, with the weights of the cube equal to the weights of the module because the total weight is zero.

The half-integer label is therefore present inside the algebra, and only in the one-sided objects: the adjoint action has integer weights, the summands have integer labels, and the ideal is a copy of $V_{3/2}$ on which only the left multiplication acts.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $P$ | a rank-one idempotent, $P^{2}=P$, $\operatorname{rank}P=1$ |
| $M_4P$ | the minimal left ideal, dimension four |
| $L_{J_z}$ | the left multiplication by the diagonal generator |
| $E_{ij}$ | the matrix unit |
| $\Lambda^3V$ | the exterior cube of the module |
| $\mathbb{P}^3$ | the projective space of lines of $\mathbb{C}^4$ |

## Further Reading

- [The Spin Group at $n=4$: the Principal Copy, $\operatorname{Sym}^3$ and the Kernel $\{\pm\mathrm I\}$](the-spin-group-at-n-4-the-principal-copy-and-its-kernel.html), for the generators and the two kernels.
- [The Four Weights of the Module and the Half Angle at $n=4$](the-four-weights-of-the-module-and-the-half-angle-at-n-4.html), for the weights of the abstract module.
- [The Exterior Cube Isomorphism $\Lambda^3V\cong V$ and $M_4(\mathbb{C})$ as $V\otimes V$](the-exterior-cube-isomorphism-lambda-3-v-v-and-m4c-as-v-tensor-v.html), for the second model.
- [The Minimal Left Ideals of the Biquaternion Algebra](the-minimal-left-ideals-of-the-biquaternion-algebra.html), for the row at order two.
- [The Minimal One-Sided Ideals, Conjugation and the Missing Label](the-minimal-one-sided-ideals-conjugation-and-the-missing-label.html), for the proof that no ideal is a summand.
