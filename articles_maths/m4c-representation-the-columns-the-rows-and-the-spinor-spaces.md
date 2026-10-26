# __$M_4(\mathbb{C})_L$ Model : Columns, Rows and the Spinor Spaces__

## Introduction

The regular module of the biquaternion algebra splits into two identical minimal left ideals. Each is a two-dimensional complex space carrying the defining representation of $M_2(\mathbb{C})$, and each is one of the two spinor spaces of *The Spinor Spaces*. In the $4\times4$ regular model the splitting is visible as two complementary coordinate planes, and the matrix acts on each plane by the same $2\times2$ matrix.

This article develops the splitting, the columns and rows, the endomorphisms and the lattice of left ideals. It is the $4\times4$ counterpart of *$M_2(\mathbb{C})$ Representation : The Columns, the Rows and the Spinor Spaces*.

**Conventions.** The algebra and the model are those of *$M_4(\mathbb{C})_L$ Representation : The Matrix Product and the Algebra Structure*. The Peirce idempotents are $\tilde\Pi_\pm=\tfrac12(e_t\pm i\vec e_z)$, the nilpotents are $\vec\Upsilon_\pm=\tfrac12(i\vec e_x\pm\vec e_y)$, and the change $S$ has columns $\tilde\Pi_+,\vec\Upsilon_+,\vec\Upsilon_-,\tilde\Pi_-$.

**Boundaries.** The Peirce coordinates are *$M_4(\mathbb{C})_L$ Representation : The Peirce Coordinates and the Matrix Units*; the spectral projectors are *$M_4(\mathbb{C})_L$ Representation : The Spectral Projectors and the Nilpotents*; the right module is *$M_4(\mathbb{C})_L$ Representation : The Centraliser and the Double Centraliser*, §*The Right Regular Image*; the abstract spinor spaces are *The Spinor Spaces*; the abstract ideals are *The Regular Module* and *The Minimal Left Ideals*. The $2\times2$ version is *$M_2(\mathbb{C})$ Representation : The Columns, the Rows and the Spinor Spaces*.

## The Left Ideals Are the Columns

**The columns of the regular matrix are the images of the basis.** The $\mu$-th column of $\mathsf{M}_4(\tilde Q)$ is $\tilde Qe_\mu$; it is the image of the $\mu$-th basis vector under the left module action. The four columns span the whole of $\mathbb{C}^4$ when $\tilde Q$ is a unit, and a two-dimensional subspace when $\tilde Q$ is a nonzero zero divisor.

**The column spaces of the projectors.** The column space of $\mathsf{M}_4(\tilde\Pi_+)$ is $E_+$; the column space of $\mathsf{M}_4(\tilde\Pi_-)$ is $E_-$. The decomposition of an arbitrary column $v$ is
$$
v=v_++v_-,\qquad v_\pm=\mathsf{M}_4(\tilde\Pi_\pm)v,
$$
and the two components are the projections on the two ideals.

**The columns of an element.** Since $\mathsf{M}_4(\tilde Q)$ preserves each ideal, its columns split according to the ideal of the corresponding basis vector. In the fixed basis the splitting is not the naive one; in the Peirce basis it is. This is the matrix form of the fact that the decomposition $\mathbb{B}=\mathbb{B}\tilde\Pi_+\oplus\mathbb{B}\tilde\Pi_-$ depends on the idempotents, not on the original basis.


**Theorem.** The algebra splits as a direct sum of left modules,

$$
\mathbb{B}=\mathbb{B}\tilde\Pi_+\oplus\mathbb{B}\tilde\Pi_-,
\qquad
\mathbb{B}\tilde\Pi_\pm\cong\mathbb{C}^2,
$$

and the two summands are minimal left ideals. Left multiplication by $\tilde Q$ preserves each summand and acts on each by the same matrix $\mathsf{M}_2(\tilde Q)$.

*Proof.* The idempotents are orthogonal and sum to $e_t$, so every $\tilde X$ splits as $\tilde X\tilde\Pi_++\tilde X\tilde\Pi_-$. The ideal $\mathbb{B}\tilde\Pi_+$ is spanned by $\tilde\Pi_+$ and $\vec\Upsilon_+$, two linearly independent elements, and the Peirce table shows that it is closed under left multiplication and has no proper nonzero submodule. The action in the basis $(\tilde\Pi_+,\vec\Upsilon_+)$ is $\mathsf{M}_2(\tilde Q)$ by the block theorem. The same holds for the second ideal in the basis $(\vec\Upsilon_-,\tilde\Pi_-)$.

**The two copies in the regular model.** In $M_4(\mathbb{C})$, the image of the first ideal is the column space of $\mathsf{M}_4(\tilde\Pi_+)$, a two-dimensional subspace $E_+\subset\mathbb{C}^4$; the second is $E_-$, the column space of $\mathsf{M}_4(\tilde\Pi_-)$. The two are complementary,
$$
\mathbb{C}^4=E_+\oplus E_-,
\qquad
E_+\cap E_-=0,
$$
and in the Peirce basis $S$ they are the coordinate planes
$$
E_+=\{(x,y,0,0)\},\qquad E_-=\{(0,0,z,w)\}.
$$
The matrix $\mathsf{M}_4(\tilde Q)$ preserves each plane and acts on both by $\mathsf{M}_2(\tilde Q)$.

**The rank of the projectors.** The projectors $\mathsf{M}_4(\tilde\Pi_\pm)$ have rank two, not rank one. The minimality of the ideals is a statement about the algebra, not about the rank of the matrix: a minimal left ideal of $\mathbb{B}$ is two complex-dimensional, and its image is a two-dimensional subspace of $\mathbb{C}^4$.

## The Rows Are the Right Ideals

**The rows are the right ideals.** The row space of $\mathsf{M}_4(\tilde Q)$ is the image of the right multiplication by $\tilde Q$ on the dual space. The right ideals of $\mathbb{B}$ are the subspaces $\tilde\Pi_\pm\mathbb{B}$, of complex dimension two, and their images are the row spaces of $\mathsf{M}_4(\tilde\Pi_\pm)$.

**The two-sided decomposition.** For every $\tilde X$,
$$
\tilde X=\sum_{i,j=1}^{2}\tilde\Pi_i\tilde X\tilde\Pi_j,
$$
the four Peirce corners. The diagonal corners are the two ideals read on the left and on the right; the off-diagonal corners are the maps between them. In the regular model the four corners become the four $2\times2$ blocks, and the off-diagonal blocks are the two copies of the nilpotent coordinates.

**The right module.** Right multiplication is an action of the opposite algebra, and the right ideals are the minimal right modules. The left and right decompositions are independent, and the regular module is a bimodule. The double centraliser statement is *$M_4(\mathbb{C})_L$ Representation : The Centraliser and the Double Centraliser*, §*The Right Regular Image*.

## Chirality and the Two Columns

**Left multiplication preserves each ideal.** For any $M$ in the image, the products $M\mathsf{M}_4(\tilde\Pi_+)$ and $M\mathsf{M}_4(\tilde\Pi_-)$ have column spaces $E_+$ and $E_-$. No left multiplication relates the two ideals. This is the matrix statement that a left ideal is stable on the left, read on the two pairs of columns.

**Right multiplication exchanges the ideals.** Right multiplication by $\vec\Upsilon_-$ maps $E_+$ onto $E_-$ and annihilates $E_-$:
$$
\mathsf{M}_4(\tilde X)\mathsf{M}_4(\vec\Upsilon_-)=\mathsf{M}_4(\tilde X\vec\Upsilon_-),
$$
and $\tilde X\vec\Upsilon_-$ lies in $\mathbb{B}\tilde\Pi_-$ for every $\tilde X$. In the Peirce basis the matrix has the two blocks
$$
\operatorname{diag}(E_{12},E_{12}),
$$
so the exchange is the block off-diagonal unit read twice, and it is not an algebra automorphism.

Read as a right multiplication, the mass term is the doubled off-diagonal block, and the two spinor spaces are exchanged simultaneously. The structural statement and the physical reading are §*The Right Action* of *The Spinor Spaces* and the $2\times2$ article.

**The exchange is not canonical.** The two ideals are isomorphic as left modules, and the isomorphism is right multiplication by a suitable element, but it depends on the choice of the off-diagonal unit. In the regular model the choice is the Peirce basis, and a different basis changes the matrix of the exchange without changing the two ideals.

## The Spinor Spaces in the Regular Model

**The two copies.** The two spinor spaces are
$$
\mathcal S=\mathbb{B}\tilde\Pi_+\cong\mathbb{C}^2,
$$
with the action of $\mathbb{B}$ by left multiplication, and $\mathcal S'=\mathbb{B}\tilde\Pi_-$ is the second. The regular module is
$$
\mathbb{B}\cong\mathcal S\oplus\mathcal S'.
$$

**The matrix form.** In the Peirce basis, a spinor is a pair $(x,y)\in\mathbb{C}^2$, and the action is
$$
\tilde Q\cdot\begin{pmatrix}x\\y\end{pmatrix}
=\mathsf{M}_2(\tilde Q)\begin{pmatrix}x\\y\end{pmatrix}.
$$
The $4\times4$ matrix acts on $E_+$ by the same formula and on $E_-$ by the same formula again. The two spinor spaces are not coupled by left multiplication; they are coupled only by right multiplication and by general endomorphisms of the regular module.

**The multiplicity.** The algebra $M_2(\mathbb{C})$ acting on itself has one isotypic component of multiplicity two: the regular module is $S^{\oplus 2}$. The multiplicity is visible in the regular model as the two blocks, and the commutant is *$M_4(\mathbb{C})_L$ Representation : The Centraliser and the Double Centraliser*.

## The Endomorphisms of the Algebra

**Theorem.** Every $\mathbb{B}$-linear endomorphism of $\mathbb{B}$ is a right multiplication, and
$$
\operatorname{End}_{\mathbb{B}}(\mathbb{B})\cong\mathbb{B}^{\mathrm{opp}}\cong M_2(\mathbb{C}),
\qquad
\dim_{\mathbb{C}}\operatorname{End}_{\mathbb{B}}(\mathbb{B})=4.
$$

*Proof.* Let $T$ be left $\mathbb{B}$-linear. Put $\tilde Q_0=T(e_t)$. For every $\tilde X$,
$$
T(\tilde X)=T(\tilde Xe_t)=\tilde XT(e_t)=\tilde X\tilde Q_0,
$$
so $T$ is right multiplication by $\tilde Q_0$. The map $\tilde Q_0\mapsto R_{\tilde Q_0}$ is an anti-isomorphism, hence an isomorphism onto the opposite algebra.

**The matrix form.** In $M_4(\mathbb{C})$ the endomorphisms are the right regular matrices $\mathsf{M}_4^{R}(\tilde Q)$, and the statement is the double centraliser theorem of *$M_4(\mathbb{C})_L$ Representation : The Centraliser and the Double Centraliser*, §*The Right Regular Image*. The two spinor spaces are exchanged by the endomorphisms that are not scalar on the multiplicity space; the scalar ones preserve each copy.

**The Hom spaces.** For the two spaces,
$$
\operatorname{Hom}_{\mathbb{B}}(\mathcal S,\mathcal S)=\mathbb{C},\qquad
\operatorname{Hom}_{\mathbb{B}}(\mathcal S,\mathcal S')=\mathbb{C},
$$
by Schur's lemma and the isomorphism $\mathcal S\cong\mathcal S'$. An endomorphism of $\mathcal S\oplus\mathcal S'$ is therefore a $2\times2$ matrix of scalars, which is the isomorphism $M_2(\mathbb{C})\cong\mathbb{B}^{\mathrm{opp}}$.

## The Lattice of Left Ideals

**The minimal ideals.** The minimal left ideals of $\mathbb{B}\cong M_2(\mathbb{C})$ are the subspaces $M_2(\mathbb{C})P$ for the rank-one projections $P$. They are parametrized by the lines of $\mathbb{C}^2$, that is, by the projective line $\mathbb{P}^1(\mathbb{C})$. Each is isomorphic to the spinor space $\mathcal S$.

**The two fixed points.** The idempotents $\tilde\Pi_+$ and $\tilde\Pi_-$ correspond to the two coordinate lines of $\mathbb{C}^2$, the two columns of the matrix model. The other minimal ideals correspond to the other lines; they are obtained from the two columns by conjugation by $GL_2(\mathbb{C})$.

**The regular model.** In $M_4(\mathbb{C})$, a minimal left ideal is a two-dimensional subspace of $\mathbb{C}^4$, the image of a rank-two projector $\mathsf{M}_4(P)$. The family is again a projective line, and the two fixed ideals $E_\pm$ are two points of it. The regular model does not add new ideals; it realizes each of them as a plane in $\mathbb{C}^4$, with the two coordinate planes as the fixed splitting.

**The lattice.** The left ideals of $\mathbb{B}$ are $0$, the minimal ideals, the sums of two distinct minimal ideals (which is $\mathbb{B}$), and $\mathbb{B}$. The lattice is the projective line with the two endpoints added, and the regular model preserves it.

## Summary

The regular module splits into two identical minimal left ideals, each a spinor space $\mathcal{S}\cong\mathbb{C}^2$. The $4\times4$ matrix preserves the two spaces and acts on each by the same $2\times2$ matrix; in the Peirce basis they are the two coordinate planes. The endomorphisms of the regular module are the right multiplications, forming the opposite algebra $M_2(\mathbb{C})$. The minimal left ideals are parametrized by the projective line, with the two columns as the fixed points.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde\Pi_\pm$ | the two minimal idempotents |
| $\mathcal S=\mathbb{B}\tilde\Pi_+$ | the first spinor space |
| $E_\pm$ | the two coordinate planes in $\mathbb{C}^4$ |
| $\operatorname{End}_{\mathbb{B}}(\mathbb{B})$ | the right multiplications |
| $\mathbb{P}^1(\mathbb{C})$ | the lattice of minimal left ideals |

## Further Reading

- [$M_4(\mathbb{C})_L$ Representation : The Peirce Coordinates and the Matrix Units](m4c-representation-the-peirce-coordinates-and-the-matrix-units.html), for the idempotents
- [$M_4(\mathbb{C})_L$ Representation : The Centraliser and the Double Centraliser](m4c-representation-the-centraliser-and-the-double-centraliser.html), §*The Right Regular Image*, for the endomorphisms
- [$M_4(\mathbb{C})_L$ Representation : Spin, Qubits and the Bloch Vector](m4c-representation-spin-qubits-and-the-bloch-vector.html), for the state space
- [$M_2(\mathbb{C})$ Representation : The Columns, the Rows and the Spinor Spaces](m2c-representation-the-columns-the-rows-and-the-spinor-spaces.html), for the $2\times2$ version
- [The Peirce Decomposition](ideals-peirce-decompositions-and-spinors-in-the-biquaternion-algebra.html), for the abstract lattice
