# __The Lie Algebra $\mathfrak{gl}_4(\mathbb{C})$ and $\mathfrak{sl}_4(\mathbb{C})$ of $M_4(\mathbb{C})$__

## Introduction

The algebra $M_4(\mathbb{C})$ is a Lie algebra under the commutator

$$
[A,B]=AB-BA,
$$

and the two Lie algebras of the category are $\mathfrak{gl}_4(\mathbb{C})=M_4(\mathbb{C})$ with this bracket, of complex dimension $16$, and its traceless ideal $\mathfrak{sl}_4(\mathbb{C})$, of dimension $15$. The first is reductive with centre $\mathbb{C}I$; the second is simple of type $A_3$. The decomposition

$$
\mathfrak{gl}_4=\mathfrak{sl}_4\oplus\mathbb{C}I
$$

is a direct sum of Lie algebras, and the trace is the only Lie homomorphism from $\mathfrak{gl}_4$ to $\mathbb{C}$.

This article states the bracket, the centre and the derived algebra, the root space decomposition of $\mathfrak{sl}_4$, the Killing form, the five real forms with their maximal compact subalgebras and signatures, and the subalgebras that the frame and the antisymmetric sector provide. The exponential and the group are *The Exponential and the Lie Group of $M_4(\mathbb{C})$*; the derivations are *The Derivations and the Automorphisms of $M_4(\mathbb{C})$*; the antisymmetric sector is *The Antisymmetric Sector, the Pfaffian and the Klein Quadric of $M_4(\mathbb{C})$*.

## The Bracket and the Decomposition

**Definition.** $\mathfrak{gl}_4(\mathbb{C})$ is the vector space $M_4(\mathbb{C})$ with the bracket $[A,B]=AB-BA$. It is a complex Lie algebra of dimension $16$.

**Proposition.** The bracket is bilinear, alternating and satisfies the Jacobi identity. The centre is $\mathbb{C}I$, and the derived algebra is

$$
[\mathfrak{gl}_4,\mathfrak{gl}_4]=\mathfrak{sl}_4=\{A:\operatorname{tr}A=0\}.
$$

**Proof.** Bilinearity and alternation are immediate from the associativity of the product. The Jacobi identity is the expansion

$$
[A,[B,C]]+[B,[C,A]]+[C,[A,B]]=0,
$$

which holds in every associative algebra. A matrix $X$ is central exactly when $XA=AX$ for all $A$, which forces $X$ to be scalar. The trace of a commutator vanishes, so the derived algebra lies in $\mathfrak{sl}_4$; the converse holds because $E_{ij}=[E_{ii},E_{ij}]$ for $i\ne j$ and $E_{ii}-E_{jj}=[E_{ij},E_{ji}]$, and these elements span the traceless matrices.

**The direct sum.** Every matrix splits as

$$
A=\bigl(A-\tfrac14\operatorname{tr}(A)I\bigr)+\tfrac14\operatorname{tr}(A)I,
$$

with the first term traceless and the second central. Both summands are ideals, and they meet in zero, so

$$
\mathfrak{gl}_4=\mathfrak{sl}_4\oplus\mathbb{C}I
$$

as Lie algebras. The centre is one-dimensional and the derived algebra is fifteen-dimensional.

**The simplicity.** $\mathfrak{sl}_4(\mathbb{C})$ is simple: it has no nonzero proper ideal.

**Proof.** The proof uses the root decomposition of the next section. Let $\mathfrak{a}\ne0$ be an ideal and let $X\in\mathfrak{a}$ be nonzero. Write $X=H_0+\sum_\alpha X_\alpha$ with $H_0\in\mathfrak{h}$ and $X_\alpha\in\mathbb{C}E_\alpha$. Choose $H\in\mathfrak{h}$ such that the numbers $\alpha(H)$ for the twelve roots and $0$ are all distinct. For a root $\alpha$, the Lagrange projector

$$
P_\alpha=\prod_{\gamma\ne\alpha}\frac{\operatorname{ad}_H-\gamma(H)}{\alpha(H)-\gamma(H)},
$$

the product running over $\{0\}\cup\{\text{roots}\}$, is a polynomial in $\operatorname{ad}_H$, so $P_\alpha(X)\in\mathfrak{a}$; and $P_\alpha(X)=X_\alpha$. If some $X_\alpha$ is nonzero, then $E_\alpha=E_{ij}\in\mathfrak{a}$ for some $i\ne j$. The brackets

$$
[E_{ij},E_{jk}]=E_{ik},\qquad [E_{ki},E_{ij}]=E_{kj},\qquad [E_{ij},E_{ji}]=E_{ii}-E_{jj}
$$

then produce every off-diagonal unit and every traceless diagonal matrix, so $\mathfrak{a}=\mathfrak{sl}_4$. If all $X_\alpha$ vanish, then $X=H_0$ is a nonzero diagonal matrix, and $[H_0,E_{ij}]=(h_i-h_j)E_{ij}\ne0$ for some $i\ne j$, so a nonzero root vector lies in $\mathfrak{a}$ and the previous case applies.

**The type.** The root system of $\mathfrak{sl}_4$ is $A_3$: rank three, twelve roots, dimension $3+12=15$.

## The Root Space Decomposition

**The Cartan subalgebra.** Let $\mathfrak{h}$ be the space of traceless diagonal matrices,

$$
\mathfrak{h}=\Bigl\{\operatorname{diag}(h_1,h_2,h_3,h_4):\sum_i h_i=0\Bigr\},
$$

of dimension $3$. It is abelian and self-normalising.

**The roots.** For $H=\operatorname{diag}(h_1,\dots,h_4)$ define the linear forms $\epsilon_i(H)=h_i$. Then

$$
[H,E_{ij}]=(h_i-h_j)E_{ij}=(\epsilon_i-\epsilon_j)(H)\,E_{ij}.
$$

The twelve forms $\pm(\epsilon_i-\epsilon_j)$, $i<j$, are the **roots**, and the **root space** of $\alpha=\epsilon_i-\epsilon_j$ is $\mathbb{C}E_{ij}$. The decomposition is

$$
\mathfrak{sl}_4=\mathfrak{h}\oplus\bigoplus_{i\ne j}\mathbb{C}E_{ij},\qquad
\dim\mathfrak{sl}_4=3+12=15.
$$

**The root lattice.** The simple roots are $\alpha_1=\epsilon_1-\epsilon_2$, $\alpha_2=\epsilon_2-\epsilon_3$ and $\alpha_3=\epsilon_3-\epsilon_4$, forming the chain of the Dynkin diagram $A_3$. The positive roots are the six forms $\epsilon_i-\epsilon_j$ with $i<j$.

**The Chevalley basis.** With $H_i=E_{ii}-E_{i+1,i+1}$ and $E_{ij}$ for $i\ne j$, the brackets are

$$
[H_i,E_{jk}]=\bigl(\delta_{ij}-\delta_{i+1,j}-\delta_{ik}+\delta_{i+1,k}\bigr)E_{jk},
$$

and

$$
[E_{ij},E_{kl}]=\delta_{jk}E_{il}-\delta_{li}E_{kj}.
$$

The matrix-unit rule gives the structure constants of $\mathfrak{sl}_4$ in this basis; for distinct $i,j,k$ it specialises to

$$
[E_{ij},E_{jk}]=E_{ik},\qquad [E_{ki},E_{ij}]=E_{kj},\qquad [E_{ij},E_{ji}]=E_{ii}-E_{jj}.
$$

**The adjoint representation.** The map $\operatorname{ad}_X(Y)=[X,Y]$ is a representation of $\mathfrak{sl}_4$ on itself, of dimension $15$, and $\mathfrak{sl}_4$ is simple, so the adjoint representation is irreducible. The weights of $\mathfrak{h}$ on $\mathfrak{sl}_4$ are the roots and zero, with multiplicities one and three.

## The Killing Form

**Definition.** The Killing form is $B(X,Y)=\operatorname{tr}(\operatorname{ad}_X\operatorname{ad}_Y)$.

**Theorem.** On $\mathfrak{gl}_4$,

$$
B(X,Y)=8\operatorname{tr}(XY)-2\operatorname{tr}(X)\operatorname{tr}(Y),
$$

and on $\mathfrak{sl}_4$ the same formula reduces to

$$
B(X,Y)=8\operatorname{tr}(XY).
$$

**Proof.** The endomorphism $\operatorname{ad}_X\operatorname{ad}_Z$ acts on the matrix unit $E_{ij}$ by

$$
\operatorname{ad}_X\operatorname{ad}_Z(E_{ij})=(x_{ii}-x_{jj})(z_{ii}-z_{jj})E_{ij},
$$

so its trace is

$$
\sum_{i,j}(x_{ii}-x_{jj})(z_{ii}-z_{jj})
=2n\operatorname{tr}(XZ)-2\operatorname{tr}(X)\operatorname{tr}(Z),
$$

which at $n=4$ is $8\operatorname{tr}(XZ)-2\operatorname{tr}X\operatorname{tr}Z$. On the traceless subspace the second term vanishes.

**The nondegeneracy.** The form is nondegenerate on $\mathfrak{sl}_4$, because $\operatorname{tr}(XY)$ is nondegenerate on the traceless matrices: if $X$ is traceless and $\operatorname{tr}(XY)=0$ for all traceless $Y$, then $X$ is a scalar, hence zero. On $\mathfrak{gl}_4$ the form is degenerate: $B(I,Y)=8\operatorname{tr}Y-2\cdot4\operatorname{tr}Y=0$ for every $Y$, so the radical is the centre $\mathbb{C}I$.

**The Casimir.** The form identifies $\mathfrak{sl}_4$ with its dual, and the inverse form gives the Casimir element of the adjoint representation, of degree two.

## The Real Forms

**Definition.** A **real form** of a complex Lie algebra $\mathfrak{g}$ is a real Lie algebra $\mathfrak{g}_0$ with $\mathfrak{g}_0\otimes_\mathbb{R}\mathbb{C}\cong\mathfrak{g}$.

**Theorem.** The real forms of $\mathfrak{sl}_4(\mathbb{C})$ are, up to isomorphism,

| Real form | Definition | $\dim$ | Maximal compact | $\dim\mathfrak{k}$ | Killing signature |
|---|---|---|---|---|---|
| $\mathfrak{su}(4)$ | $\{X:X^{*}=-X,\ \operatorname{tr}X=0\}$ | $15$ | $\mathfrak{su}(4)$ | $15$ | $(0,15)$ |
| $\mathfrak{su}(1,3)$ | $\{X:X^{*}J+JX=0,\ \operatorname{tr}X=0\}$ | $15$ | $\mathfrak{u}(3)$ | $9$ | $(6,9)$ |
| $\mathfrak{su}(2,2)$ | $\{X:X^{*}J+JX=0,\ \operatorname{tr}X=0\}$ | $15$ | $\mathfrak{s}(\mathfrak{u}(2)\oplus\mathfrak{u}(2))$ | $7$ | $(8,7)$ |
| $\mathfrak{sl}_4(\mathbb{R})$ | the real traceless matrices | $15$ | $\mathfrak{so}(4)$ | $6$ | $(9,6)$ |
| $\mathfrak{su}^{*}(4)=\mathfrak{sl}_2(\mathbb{H})$ | the quaternionic traceless matrices | $15$ | $\mathfrak{sp}(2)$ | $10$ | $(5,10)$ |

In the table $J$ is the form $\operatorname{diag}(1,-1,-1,-1)$ for $\mathfrak{su}(1,3)$ and $\operatorname{diag}(1,1,-1,-1)$ for $\mathfrak{su}(2,2)$; $\mathfrak{su}^{*}(4)$ is the algebra of $2\times2$ quaternionic matrices with $\operatorname{Re}\operatorname{tr}X=0$.

**The compact form.** $\mathfrak{su}(4)$ is the compact real form: $X^{*}=-X$ makes the Killing form negative definite. Its complexification is $\mathfrak{sl}_4$, and the conjugation is $X\mapsto -X^{*}$.

**The signatures.** For a real form with Cartan involution $\theta$, the form $B_\theta(X,Y)=-B(X,\theta Y)$ is positive definite, $B$ is negative definite on the fixed algebra $\mathfrak{k}$ and positive definite on its complement $\mathfrak{p}$. The signature column is $(\dim\mathfrak{p},\dim\mathfrak{k})$, with $\dim\mathfrak{p}+\dim\mathfrak{k}=15$.

**The symmetric spaces.** The Cartan decompositions give

$$
SU(4)/S(U(1)\times U(3))=\mathbb{CP}^{3},\qquad
SU(1,3)/S(U(1)\times U(3))=\mathbb{CH}^{3},
$$

of real dimension $6$, and

$$
SU(2,2)/S(U(2)\times U(2)),\qquad
SL_4(\mathbb{R})/SO(4),\qquad
SU^{*}(4)/Sp(2)=H^{5},
$$

of real dimensions $8$, $9$ and $5$. The first two are the compact and non-compact complex projective spaces; the third is the Grassmannian of two-planes of signature $(2,2)$; the fourth is the space of positive definite symmetric matrices of determinant one; the fifth is the real hyperbolic five-space.

**The isomorphisms.** $\mathfrak{su}(2,2)\cong\mathfrak{so}(2,4)$, of dimension $15$: the conformal algebra of four-dimensional Minkowski space. $\mathfrak{su}^{*}(4)\cong\mathfrak{so}(5,1)$, the isometry algebra of hyperbolic five-space. $\mathfrak{su}(1,3)$ is the isometry algebra of the indefinite Hermitian form of signature $(1,3)$, and it is the algebra of the Krein isometries of *The Krein Isometry Group and Its Cartan Decomposition*.

## The Subalgebras of the Category

**The antisymmetric sector.** The antisymmetric matrices form $\mathfrak{so}(4,\mathbb{C})\subset\mathfrak{sl}_4$, of dimension $6$, and

$$
\mathfrak{so}(4,\mathbb{C})=\Lambda^{2}_{+}\oplus\Lambda^{2}_{-}\cong\mathfrak{sl}_2\oplus\mathfrak{sl}_2.
$$

The two summands are the self-dual and anti-self-dual halves of *The Antisymmetric Sector, the Pfaffian and the Klein Quadric of $M_4(\mathbb{C})$*, and the splitting is the one attached to the Hodge star.

**The chiral pair.** The diagonal subalgebra

$$
\mathfrak{s}(\mathfrak{u}(2)\oplus\mathfrak{u}(2))=\Bigl\{\begin{pmatrix}A&0\\0&D\end{pmatrix}:\operatorname{tr}A+\operatorname{tr}D=0\Bigr\}
$$

is the compact algebra of the chiral decomposition of the carrier, of dimension $7$. It is $\mathfrak{su}(2)\oplus\mathfrak{su}(2)\oplus\mathfrak{u}(1)$, and the semisimple part $\mathfrak{su}(2)\oplus\mathfrak{su}(2)$ is the chiral pair that preserves the chiral splitting of *The Peirce $\mathfrak{su}_2$ and the Chiral $\mathfrak{su}_2\times\mathfrak{su}_2$ of $M_4(\mathbb{C})$*.

**The Peirce chain.** The three matrices $J_3=\operatorname{diag}(\tfrac32,\tfrac12,-\tfrac12,-\tfrac32)$ and $J_\pm$ of the principal $\mathfrak{sl}_2$ generate a copy of $\mathfrak{sl}_2$ inside $\mathfrak{sl}_4$, acting irreducibly on $\mathbb{C}^{4}$ as the highest-weight-$\tfrac32$ representation. It is generated by the simple nilpotents, and it is not the chiral pair: the chain mixes the two chiralities, the pair preserves them.

**The dimensions.** The three subalgebras have dimensions $6$, $7$ and $3$; the first is the antisymmetric sector, the second preserves the chiral splitting, and the third acts irreducibly on $\mathbb{C}^{4}$. None of them is contained in another: the antisymmetric sector has no diagonal matrices, the chiral pair is not antisymmetric, and the chain has both diagonal and block-mixing off-diagonal matrices.

## Summary

$\mathfrak{gl}_4(\mathbb{C})$ is the sixteen-dimensional Lie algebra of $4\times4$ matrices under the commutator, with centre $\mathbb{C}I$ and derived algebra $\mathfrak{sl}_4$, so that $\mathfrak{gl}_4=\mathfrak{sl}_4\oplus\mathbb{C}I$. $\mathfrak{sl}_4$ is simple of type $A_3$, of dimension $15$, with a Cartan subalgebra of dimension $3$ and twelve roots $\pm(\epsilon_i-\epsilon_j)$ carried by the matrix units $E_{ij}$. Its Killing form is $8\operatorname{tr}(XY)$, and the form on $\mathfrak{gl}_4$ is $8\operatorname{tr}(XY)-2\operatorname{tr}X\operatorname{tr}Y$. The five real forms are $\mathfrak{su}(4)$, $\mathfrak{su}(1,3)$, $\mathfrak{su}(2,2)$, $\mathfrak{sl}_4(\mathbb{R})$ and $\mathfrak{su}^{*}(4)$, of maximal compact dimensions $15$, $9$, $7$, $6$ and $10$, with Killing signatures $(0,15)$, $(6,9)$, $(8,7)$, $(9,6)$ and $(5,10)$. The antisymmetric sector, the chiral pair and the principal $\mathfrak{sl}_2$ are subalgebras of dimensions $6$, $7$ and $3$.

| Quantity | Value |
|---|---|
| $\dim_\mathbb{C}\mathfrak{gl}_4$ | $16$ |
| $\dim_\mathbb{C}\mathfrak{sl}_4$ | $15$ |
| $\dim\mathfrak{h}$ | $3$ |
| Number of roots | $12$ |
| $B(X,Y)$ on $\mathfrak{sl}_4$ | $8\operatorname{tr}(XY)$ |
| Real forms | $5$ |
| $\dim\mathfrak{so}(4,\mathbb{C})$ | $6$ |
| $\dim\mathfrak{su}(2)\oplus\mathfrak{su}(2)$ | $6$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathfrak{gl}_4$ | $M_4(\mathbb{C})$ with the commutator |
| $\mathfrak{sl}_4$ | the traceless matrices, the derived algebra |
| $\mathfrak{h}$ | the traceless diagonal matrices |
| $\epsilon_i$ | the linear form $\operatorname{diag}(h_1,\dots,h_4)\mapsto h_i$ |
| $\alpha_i$ | the simple roots $\epsilon_i-\epsilon_{i+1}$ |
| $B$ | the Killing form |
| $\mathfrak{k},\mathfrak{p}$ | the compact and non-compact parts of a Cartan decomposition |
| $\Lambda^{2}_{\pm}$ | the self-dual and anti-self-dual subalgebras of $\mathfrak{so}(4,\mathbb{C})$ |

## Further Reading

- [The Sylvester Operator and the Kronecker Sum of $M_4(\mathbb{C})$](the-sylvester-operator-and-the-kronecker-sum-of-m4c.html), for the adjoint operator $\operatorname{ad}_A$ and the root values.
- [The Matrix Algebra $M_4(\mathbb{C})$](the-matrix-algebra-m4c.html), for the algebra, the trace and the centre.
- [The Exponential and the Lie Group of $M_4(\mathbb{C})$](the-exponential-and-the-lie-group-of-m4c.html), for the group and the exponential.
- [The Derivations and the Automorphisms of $M_4(\mathbb{C})$](the-derivations-and-the-automorphisms-of-m4c.html), for $\operatorname{Der}(M_4)=\operatorname{ad}\mathfrak{sl}_4$.
- [The Antisymmetric Sector, the Pfaffian and the Klein Quadric of $M_4(\mathbb{C})$](the-antisymmetric-sector-the-pfaffian-and-the-klein-quadric-of-m4c.html), for $\mathfrak{so}(4,\mathbb{C})=\mathfrak{sl}_2\oplus\mathfrak{sl}_2$.
- [The Peirce $\mathfrak{su}_2$ and the Chiral $\mathfrak{su}_2\times\mathfrak{su}_2$ of $M_4(\mathbb{C})$](the-peirce-su2-and-the-chiral-su2-su2-of-m4c.html), for the chiral pair.
- James E. Humphreys, *Introduction to Lie Algebras and Representation Theory* (Springer, 1972), for the root systems and the Killing form.
- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (AMS, 2001), for the real forms and the Cartan decompositions.
