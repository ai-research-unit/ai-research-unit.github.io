# __The Adjoint of the Peirce Projection__

## Introduction

The Peirce projection of an idempotent $e$ is the operator $P_e(x)=exe$, the projection of $A$ onto the corner $eAe$ along the other three Peirce corners. When $A$ carries a form, the operator has an adjoint, and the adjoint is again a Peirce projection:

$$
P_e^\dagger=P_{e^*},
$$

where $e^*$ is the adjoint of the idempotent with respect to the form. The identity is the operator form of the element adjoint. It says that the Peirce projection onto the corner of $e$ is adjoint to the Peirce projection onto the corner of $e^*$, and it reduces the question of whether $P_e$ is an orthogonal projection to the question of whether $e$ is Hermitian: $P_e$ is self-adjoint exactly when $e^*=e$.

The consequence is the orthogonal Peirce decomposition. If $e$ is Hermitian, all four Peirce projections are self-adjoint, the four corners are pairwise orthogonal, and the decomposition

$$
A=eAe\oplus eAf\oplus fAe\oplus fAf
$$

is an orthogonal direct sum. If $e$ is not Hermitian, $P_e$ is not self-adjoint, the corners need not be orthogonal, and the form may pair the corner of $e$ with the corner of $e^*$; the symplectic matrix algebra and the split algebra with the exchange involution are the standard examples. The article proves the adjoint identity, the kernel–image form of it, and the orthogonal Peirce theorem, and it computes the three cases.

The article is the form-theoretic companion of *The Sandwich Operators on the Peirce Components*, *Left and Right Multiplication on the Diagonal Peirce Part* and *Idempotents and Involutions of an Algebra*. The Peirce decomposition is that of *Unital Algebras*, §*Idempotents and the Peirce Decomposition*; the involutions are *Involutive Algebras*; the Hermitian idempotents and their Peirce theory are *Hermitian Idempotents and the Peirce Decomposition*; the form theory is *Hermitian Forms on a Sesqualgebra* and *Hermitian Forms over Algebras and Norms*; and the matrix and symplectic examples are *Matrix Algebras* and *The Unitary and Symplectic Groups*. The article uses no positivity and no topology.

Throughout, $k$ is a field, $A$ is a finite-dimensional unital associative $k$-algebra with $1\neq0$, and $*$ is an involution of $A$. The form $\langle-,-\rangle:A\times A\to k$ is nondegenerate and **associative Hermitian**: for all $a,x,y\in A$,

$$
\langle ax,y\rangle=\langle x,a^*y\rangle, \qquad \langle xa,y\rangle=\langle x,ya^*\rangle.
$$

The form is written bilinear; if it is sesquilinear over a field with a conjugation, the same identities hold with the scalar conjugation absorbed in the notation, and the operator adjoint is conjugate-linear in the operator. The article does not use the distinction. The idempotent is $e$, its complement is $f=1-e$, the corners are $A_{ij}=e_iAe_j$ with $e_0=e$, $e_1=f$, and the Peirce projections are $E_{ij}=T_{e_i,e_j}$. The operator adjoint is written $\dagger$; the algebra involution is written $*$. They are different maps: $*$ acts on $A$, and $\dagger$ acts on $\operatorname{End}_k(A)$.

## The Form and the Adjoint

### The associative Hermitian form

**Definition.** A **Hermitian form** on the involutive algebra $(A,*)$ is a nondegenerate form satisfying the two adjunction identities above. The first identity says that the adjoint of left multiplication by $a$ is left multiplication by $a^*$; the second says the same for right multiplication. The two identities are the form-level statement that $*$ is an involution of the algebra and that the form is compatible with the multiplication.

**Example (the trace form).** Let $A=M_n(k)$ with an involution $*$ (transpose, conjugate transpose, symplectic, or any other). The form

$$
\langle X,Y\rangle=\operatorname{tr}(X^*Y)
$$

is nondegenerate and associative Hermitian: $(AX)^*=X^*A^*$ gives

$$
\langle AX,Y\rangle=\operatorname{tr}(X^*A^*Y)=\langle X,A^*Y\rangle,
$$

and the second identity is the same computation with the cyclic property of the trace. The form is the **Hermitian trace form** of the involution. For the transpose it is the standard bilinear dot product on the matrix entries; for the conjugate transpose it is the Hilbert–Schmidt form; for the symplectic involution it is the symplectic trace form.

**Example (the split algebra).** Let $A=k\times k$ with the exchange involution $(a,b)^*=(b,a)$, and let

$$
\langle (a,b),(c,d)\rangle=ad+bc.
$$

Then

$$
\langle (a,b)(x,y),(c,d)\rangle=\langle (ax,by),(c,d)\rangle=axd+byc,
$$

and

$$
\langle (x,y),(a,b)^*(c,d)\rangle=\langle (x,y),(bc,ad)\rangle=xad+ybc,
$$

so the first identity holds; the second is the same. The form is the hyperbolic form of the two coordinates, and it is nondegenerate: the matrix of the form in the basis $e=(1,0),f=(0,1)$ is $\begin{pmatrix}0&1\\1&0\end{pmatrix}$.

### The operator adjoint

**Definition.** For $T\in\operatorname{End}_k(A)$, the **adjoint** $T^\dagger$ is the unique operator with

$$
\langle T x,y\rangle=\langle x,T^\dagger y\rangle \qquad\text{for all }x,y\in A.
$$

Existence and uniqueness are the nondegeneracy of the form in finite dimension: the map $y\mapsto\langle-,y\rangle$ is an isomorphism $A\to A^\vee$, and $T^\dagger$ is the transpose of $T$ transported across it.

**Proposition.** The adjoint operation on $\operatorname{End}_k(A)$ satisfies

$$
\boxed{\;(T+S)^\dagger=T^\dagger+S^\dagger, \qquad (TS)^\dagger=S^\dagger T^\dagger, \qquad (T^\dagger)^\dagger=T, \qquad \mathrm{id}^\dagger=\mathrm{id}\;}.
$$

It is an anti-involution of the operator algebra. If the form is sesquilinear, it is conjugate-linear in the scalar; the four identities are unchanged.

*Proof.* The first and the last are immediate. For the product, $\langle TSx,y\rangle=\langle Sx,T^\dagger y\rangle=\langle x,S^\dagger T^\dagger y\rangle$. For the double adjoint, $\langle T^\dagger x,y\rangle=\langle x,Ty\rangle$ by the defining identity applied to $T^\dagger$ and the symmetry of the form; uniqueness gives $(T^\dagger)^\dagger=T$.

### The adjoints of left and right multiplication

**Theorem.** For all $a,b\in A$:

**(a)** $L_a^\dagger=L_{a^*}$.

**(b)** $R_a^\dagger=R_{a^*}$.

**(c)** $T_{a,b}^\dagger=T_{a^*,b^*}$.

**(d)** $P_e^\dagger=P_{e^*}$.

*Proof.* (a) $\langle L_a x,y\rangle=\langle ax,y\rangle=\langle x,a^*y\rangle=\langle x,L_{a^*}y\rangle$. (b) $\langle R_a x,y\rangle=\langle xa,y\rangle=\langle x,ya^*\rangle=\langle x,R_{a^*}y\rangle$. (c) $T_{a,b}=L_aR_b$, so $T_{a,b}^\dagger=R_b^\dagger L_a^\dagger=R_{b^*}L_{a^*}=L_{a^*}R_{b^*}=T_{a^*,b^*}$, using the commutativity of left and right multiplication. (d) $P_e=T_{e,e}$, so $P_e^\dagger=T_{e^*,e^*}=P_{e^*}$.

**Corollary.** The Peirce projection of $e$ is self-adjoint exactly when $e$ is Hermitian:

$$
\boxed{\;P_e^\dagger=P_e \iff e^*=e\;}.
$$

*Proof.* If $P_e^\dagger=P_e$, then $P_{e^*}=P_e$; applying both sides to $1$ gives $e^*=e$. Conversely, if $e^*=e$, then $P_e^\dagger=P_{e^*}=P_e$.

**Remark.** The theorem is the operator form of the element adjoint. The involution $*$ sends the idempotent $e$ to the idempotent $e^*$; the operator adjoint $\dagger$ sends the Peirce projection $P_e$ to the Peirce projection $P_{e^*}$. The two maps are compatible, and the compatibility is the identity \(P_e^\dagger=P_{e^*}\). The reader should keep the two stars apart: $e^*$ is an element of $A$, and $P_e^\dagger$ is an operator on $A$.

## The Adjoint of the Peirce Projection

### The identity

The Peirce projection is

$$
P_e=T_{e,e}:A\longrightarrow A, \qquad P_e(x)=exe.
$$

It is the projection onto $A_{00}=eAe$ along $N=A_{01}\oplus A_{10}\oplus A_{11}$. Its adjoint is the Peirce projection of the adjoint idempotent:

$$
P_e^\dagger=P_{e^*}:A\longrightarrow A, \qquad P_e^\dagger(y)=e^*ye^*.
$$

The identity is the main theorem of the article, and it has three readings:

- **Operator reading.** The adjoint of the projection onto the corner of $e$ is the projection onto the corner of $e^*$.
- **Element reading.** The adjoint of the idempotent $e$ is the idempotent $e^*$; the Peirce projection is the operator that records the corner, and the adjoint records the adjoint corner.
- **Form reading.** The corner $eAe$ and the corner $e^*Ae^*$ are the images of the two adjoint projections; the form pairs the first with the dual of the second, and the kernel of one is the orthogonal complement of the image of the other.

### Kernel and image

**Theorem.** Let $P=P_e$.

**(a)** $\ker P=(\operatorname{im}P^\dagger)^\perp=(e^*Ae^*)^\perp$.

**(b)** $\operatorname{im}P=(\ker P^\dagger)^\perp$.

**(c)** If $e$ is Hermitian, $\ker P=(eAe)^\perp$ and $\operatorname{im}P=(\ker P)^\perp$; the projection is orthogonal.

**(d)** If $e$ is not Hermitian, $P$ is not self-adjoint, and the kernel of $P$ is the orthogonal complement of the adjoint corner $e^*Ae^*$, not of $eAe$. The Peirce decomposition is then not orthogonal in general.

*Proof.* (a) For any operator $T$, $x\in\ker T$ iff $\langle Tx,y\rangle=0$ for all $y$ iff $\langle x,T^\dagger y\rangle=0$ for all $y$ iff $x\in(\operatorname{im}T^\dagger)^\perp$. Apply this to $T=P$ and use $P^\dagger=P_{e^*}$, whose image is $e^*Ae^*$. (b) is the same statement applied to $P^\dagger$. (c) If $e=e^*$, then $P^\dagger=P$, so $\ker P=(\operatorname{im}P)^\perp$ and $\operatorname{im}P=(\ker P)^\perp$. (d) If $P\neq P^\dagger$, the projection is not orthogonal, and (a) identifies its kernel with the orthogonal complement of the adjoint corner.

**Remark.** The identity \(\ker P_e=(e^*Ae^*)^\perp\) is the precise sense in which the Peirce decomposition is not orthogonal when $e$ is not Hermitian: the kernel of the projection onto $eAe$ is the orthogonal complement of the **adjoint** corner, not of $eAe$ itself. When $e$ is Hermitian the two corners coincide, and the kernel is the orthogonal complement of the corner, as an orthogonal projection requires.

### The Hermitian case: orthogonal Peirce decomposition

**Theorem.** Suppose $e$ is Hermitian. Then:

**(a)** Each Peirce projection $E_{ij}=T_{e_i,e_j}$ is self-adjoint.

**(b)** The four Peirce projections are pairwise orthogonal, and the four corners are pairwise orthogonal.

**(c)** The Peirce decomposition is an orthogonal direct sum,

$$
A=A_{00}\oplus A_{01}\oplus A_{10}\oplus A_{11},
$$

and the form restricts to a nondegenerate form on each corner.

**(d)** $P_e=E_{00}$ is the orthogonal projection onto $eAe$, and $P_f=E_{11}$ is the orthogonal projection onto $fAf$.

*Proof.* (a) $E_{ij}^\dagger=T_{e_i^*,e_j^*}=T_{e_i,e_j}=E_{ij}$, because $e$ and $f=1-e$ are Hermitian. (b) The $E_{ij}$ are idempotent and self-adjoint by (a), and they satisfy $E_{ij}E_{kl}=\delta_{ik}\delta_{jl}E_{ij}$; hence they are pairwise orthogonal projections. Their images are the corners, so the corners are pairwise orthogonal. (c) The sum of the $E_{ij}$ is the identity, so the corners span $A$; with (b) the sum is orthogonal. The restriction of a nondegenerate form to an orthogonal direct summand is nondegenerate, because a vector in the radical of the summand is orthogonal to the summand and to all the other summands, hence to $A$. (d) is the special case $(i,j)=(0,0)$ and $(1,1)$.

**Corollary (the orthogonal Peirce decomposition).** For a Hermitian idempotent $e$,

$$
\boxed{\;A=eAe\ \perp\ eAf\ \perp\ fAe\ \perp\ fAf\;},
$$

and the orthogonal projection onto $eAe$ is $P_e(x)=exe$. The decomposition is the orthogonal form of the Peirce decomposition of *Hermitian Idempotents and the Peirce Decomposition*.

**Remark.** The theorem is the reason the Hermitian idempotents are the algebra-level analogues of the orthogonal projections. The Peirce projection $P_e$ is self-adjoint, its image is the corner, and its kernel is the orthogonal complement of the corner. The two mixed corners $eAf$ and $fAe$ are exchanged by the involution, and they are orthogonal to each other under the form.

**Example (the Hilbert–Schmidt form).** Let $A=M_2(\mathbb{C})$ with the conjugate transpose and $\langle X,Y\rangle=\operatorname{tr}(X^*Y)$, and let $e=E_{11}$. The idempotent is Hermitian, $P_e(X)=E_{11}XE_{11}$ is the orthogonal projection onto the $(1,1)$ entry, and the four corners are the four complex lines $E_{11},E_{12},E_{21},E_{22}$. The mixed corners are orthogonal, $\langle E_{12},E_{21}\rangle=\operatorname{tr}(E_{21}E_{21})=0$, and the Peirce decomposition is the orthogonal direct sum of the four lines. The example is the positive definite model of the theorem; the symplectic and split examples below show what changes when the idempotent is not Hermitian.

### The non-Hermitian case

When $e$ is not Hermitian, the Peirce projection is not self-adjoint, and the corners need not be orthogonal. The form pairs the corner of $e$ with the corner of $e^*$, and the two extreme examples are the symplectic matrix algebra and the split algebra with the exchange involution.

**Example (the symplectic matrix algebra).** Let $A=M_2(k)$ with the symplectic involution

$$
X^*=JX^{\mathsf T}J^{-1}, \qquad J=\begin{pmatrix}0&1\\-1&0\end{pmatrix},
$$

and the form $\langle X,Y\rangle=\operatorname{tr}(X^*Y)$. Let $e=E_{11}$, so $e^*=E_{22}=f$. The Peirce projection is $P_e(X)=E_{11}XE_{11}$, the projection onto the $(1,1)$ entry, and its adjoint is $P_f$, the projection onto the $(2,2)$ entry. The corners are the four lines

$$
A_{00}=kE_{11}, \quad A_{01}=kE_{12}, \quad A_{10}=kE_{21}, \quad A_{11}=kE_{22}.
$$

The form is hyperbolic on the pairs: $E_{11}$ and $E_{22}$ are isotropic and satisfy $\langle E_{11},E_{22}\rangle=1$, while $E_{12}$ and $E_{21}$ satisfy $\langle E_{12},E_{21}\rangle=-1$ and are isotropic. The Peirce decomposition is therefore not orthogonal; it is a hyperbolic pairing of the two diagonal corners and of the two mixed corners. The projection $P_e$ is not self-adjoint, and $P_e^\dagger=P_f$.

**Example (the split algebra).** Let $A=k\times k$ with the exchange involution and the hyperbolic form $\langle (a,b),(c,d)\rangle=ad+bc$. Let $e=(1,0)$, so $e^*=(0,1)=f$. The Peirce projection is $P_e(x_0,x_1)=(x_0,0)$, and its adjoint is $P_f(x_0,x_1)=(0,x_1)$. The two coordinate lines are isotropic and paired, and the Peirce decomposition is not orthogonal. The example is the commutative model of the symplectic one: the exchange involution and the hyperbolic form produce the same pairing of the two corners.

**Remark (the two diagonal projections).** In both examples, $P_e$ and $P_f$ are adjoint projections: $P_eP_f=P_fP_e=0$, and $P_e+P_f=E_{00}+E_{11}$ is the projection onto the diagonal part $D=A_{00}\oplus A_{11}$. In the Hermitian case the two projections are orthogonal; in the non-Hermitian case they are adjoint but not self-adjoint, and the form pairs their images. The pair is the simplest example of a dual pair of projections in the sense of the form.

## Summary

Let $A$ be a finite-dimensional involutive algebra with a nondegenerate associative Hermitian form. The operator adjoint $\dagger$ satisfies $L_a^\dagger=L_{a^*}$, $R_a^\dagger=R_{a^*}$ and $T_{a,b}^\dagger=T_{a^*,b^*}$. For an idempotent $e$, the Peirce projection $P_e=T_{e,e}$ has adjoint \(P_e^\dagger=P_{e^*}\), the Peirce projection of the adjoint idempotent. Hence $P_e$ is self-adjoint exactly when $e$ is Hermitian. The kernel of $P_e$ is the orthogonal complement of the image of $P_{e^*}$, that is, $(e^*Ae^*)^\perp$; the image of $P_e$ is the orthogonal complement of the kernel of $P_{e^*}$. When $e$ is Hermitian, all four Peirce projections $E_{ij}$ are self-adjoint, the four corners are pairwise orthogonal, the Peirce decomposition is an orthogonal direct sum, and $P_e$ is the orthogonal projection onto $eAe$. When $e$ is not Hermitian, the Peirce projection is not self-adjoint, the corners need not be orthogonal, and the form pairs the corner of $e$ with the corner of $e^*$: the symplectic matrix algebra and the split algebra with the exchange involution are the models, with isotropic corners and hyperbolic pairings. The article uses no positivity and no topology.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $*$ | the algebra involution, $a\mapsto a^*$ |
| $\dagger$ | the operator adjoint, $T\mapsto T^\dagger$ |
| $\langle-,-\rangle$ | the associative Hermitian form |
| $L_a,R_a$ | left and right multiplication |
| $T_{a,b}=L_aR_b$ | the sandwich $x\mapsto axb$ |
| $P_e=T_{e,e}$ | the Peirce projection onto $eAe$ |
| $E_{ij}=T_{e_i,e_j}$ | the Peirce projection onto $A_{ij}$ |
| $e^*$ | the adjoint idempotent |
| $P_e^\dagger=P_{e^*}$ | the adjoint Peirce projection |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the Peirce decomposition and the projections onto the corners.
- Nathan Jacobson, *Basic Algebra II* (Freeman, 1989), for involutions, Hermitian forms and the classical matrix algebras.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the involutions and the Hermitian forms of the classical algebras.
- Israel Gohberg, Peter Lancaster and Leiba Rodman, *Indefinite Linear Algebra and Applications* (Birkhäuser, 2005), for the indefinite and symplectic forms and the dual pairs of projections.
