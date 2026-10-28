# __The Spinor Spaces__

## Introduction

The Peirce frame cuts the algebra into four lines. Two pairings of these lines give two planes, and each plane is a spinor space. This article defines the two planes, gives the couples of Peirce vectors that span them, computes the left action on each couple, states how right multiplication exchanges them, and reads the weights of the frame root, which are $\pm\tfrac12$: each plane is a spin-$\tfrac12$ carrier.

The article assumes *The Peirce Decomposition* and nothing else: the product, the complete orthogonal pair of idempotents, the Peirce table and the two mixed units. It uses no form, no norm and no module. The spin weights are read from the left action alone.

The module reading of the same two planes — that they are the minimal left ideals, that they are isomorphic, that they are the simple module — is *The Minimal Left Ideals*. There the two planes acquire a second job; here they have only their Peirce job.

## The Two Spinor Spaces

**The two planes $\mathbb{B}\tilde\Pi_+$ and $\mathbb{B}\tilde\Pi_-$ are the spinor spaces of the frame; each is spanned by one idempotent and one nilpotent, and the algebra is their direct sum as a vector space.**

Fix the complete orthogonal pair $\tilde\Pi_+,\tilde\Pi_-$ of a root of $+1$ and the Peirce basis $\mathcal{P}=(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-)$ of §*The Biquaternion Case* of *The Peirce Decomposition*, with $\vec\Upsilon_-\in\mathbb{B}_{+-}$ and $\vec\Upsilon_+\in\mathbb{B}_{-+}$. The two **spinor spaces** are

$$
S_+=\mathbb{B}\tilde\Pi_+=\mathbb{B}_{++}\oplus\mathbb{B}_{-+}=\mathbb{C}\tilde\Pi_+\oplus\mathbb{C}\vec\Upsilon_+,
\qquad
S_-=\mathbb{B}\tilde\Pi_-=\mathbb{B}_{+-}\oplus\mathbb{B}_{--}=\mathbb{C}\vec\Upsilon_-\oplus\mathbb{C}\tilde\Pi_- .
$$

A **spinor of first chirality** is a coordinate $(\alpha,\beta)$ on $S_+$, written in the couple as the representative $\alpha\tilde\Pi_++\beta\vec\Upsilon_+$; a **spinor of second chirality** is a coordinate $(\gamma,\delta)$ on $S_-$, written $\gamma\vec\Upsilon_-+\delta\tilde\Pi_-$. Each space has complex dimension two and real dimension four.

**The direct sum.** Every $\tilde X\in\mathbb{B}$ satisfies $\tilde X=\tilde X(\tilde\Pi_++\tilde\Pi_-)=\tilde X\tilde\Pi_++\tilde X\tilde\Pi_-$, so the two spaces span. Their intersection is zero: if $\tilde Y=\tilde Y\tilde\Pi_+=\tilde Y\tilde\Pi_-$, then $\tilde Y=\tilde Y\tilde\Pi_+=\tilde Y\tilde\Pi_-\tilde\Pi_+=0$. Hence

$$
\mathbb{B}=S_+\oplus S_- .
$$

The two spaces are distinct subspaces of the algebra. The labels record which idempotent generates the space, not a property of the space on its own.

## The Two Couples

**The Peirce basis splits into two couples, each a basis of one spinor space adapted to the element; the two couplings are the two halves of the frame.**

The four Peirce vectors form the two **couples**

$$
\mathcal{C}_+=(\tilde\Pi_+,\ \vec\Upsilon_+),
\qquad
\mathcal{C}_-=(\vec\Upsilon_-,\ \tilde\Pi_-),
$$

each made of one idempotent and one nilpotent, and each a basis of its spinor space. They are the two halves of $\mathcal{P}$. For the standard pair $\vec\Upsilon_-=\vec\Upsilon_x$ and $\vec\Upsilon_+=\vec\Upsilon_y$, so that $\mathcal{C}_+=(\tilde\Pi_+,\vec\Upsilon_y)$ and $\mathcal{C}_-=(\vec\Upsilon_x,\tilde\Pi_-)$.

The two mixed units multiply the couples together:

$$
\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+,
\qquad
\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-,
$$

which is the multiplication table of §*The Biquaternion Case* of *The Peirce Decomposition*.

**Every element is a pair of spinor coordinates.** The splitting of the algebra gives

$$
\tilde X=\tilde X\tilde\Pi_++\tilde X\tilde\Pi_-,
\qquad
\tilde X\tilde\Pi_+\in S_+,\quad\tilde X\tilde\Pi_-\in S_- .
$$

The decomposition is a decomposition of the element, not of the algebra only: it names the two spinor components of $\tilde X$.

## The Left Action on Each Couple

**Left multiplication preserves each spinor space, and in the two couples it has the same matrix, the Peirce matrix of the multiplier.**

Let $\tilde P$ have the Peirce expansion

$$
\tilde P=p_{11}\tilde\Pi_++p_{12}\vec\Upsilon_-+p_{21}\vec\Upsilon_++p_{22}\tilde\Pi_-,
\qquad
\mathsf M(\tilde P)=\begin{pmatrix}p_{11}&p_{12}\\p_{21}&p_{22}\end{pmatrix}.
$$

**Proposition.** In the basis $\mathcal{C}_+$ of $S_+$ and in the basis $\mathcal{C}_-$ of $S_-$,

$$
L_{\tilde P}|_{S_+}=\mathsf M(\tilde P),
\qquad
L_{\tilde P}|_{S_-}=\mathsf M(\tilde P).
$$

*Proof.* From the Peirce table, in $S_+$,

$$
\tilde P\tilde\Pi_+=p_{11}\tilde\Pi_++p_{21}\vec\Upsilon_+,
\qquad
\tilde P\vec\Upsilon_+=p_{12}\tilde\Pi_++p_{22}\vec\Upsilon_+,
$$

and in $S_-$,

$$
\tilde P\vec\Upsilon_-=p_{11}\vec\Upsilon_-+p_{21}\tilde\Pi_-,
\qquad
\tilde P\tilde\Pi_-=p_{12}\vec\Upsilon_-+p_{22}\tilde\Pi_- .
$$

In each couple the first basis vector has the column $(p_{11},p_{21})$ and the second the column $(p_{12},p_{22})$, which are the two columns of $\mathsf M(\tilde P)$.

The two spaces are closed on the left, $\mathbb{B}S_\pm\subseteq S_\pm$, because $S_\pm=\mathbb{B}\tilde\Pi_\pm$ and the multiplication is associative. Left multiplication therefore never mixes the two chiralities.

**Remark (chirality is not a scalar of left multiplication).** Inside a couple, left multiplication mixes the idempotent and the nilpotent whenever $p_{12}$ or $p_{21}$ is nonzero. A basis vector is carried to a multiple of itself exactly when the coefficient that couples it to the other member of its couple vanishes; both are carried to multiples exactly when $\mathsf M(\tilde P)$ is diagonal.

## The Root on a Couple

**The frame root acts on both couples by the same diagonal matrix $\operatorname{diag}(1,-1)$; the half-root has weights $\pm\tfrac12$, so each plane is a spin-$\tfrac12$ carrier, while the right root is the chirality scalar $+1$ on $S_+$ and $-1$ on $S_-$.**

**The weights.** The root is $\tilde\Xi=\tilde\Pi_+-\tilde\Pi_-$. The corner signs of *The Peirce Decomposition* give, in the couple $\mathcal{C}_+$,

$$
L_{\tilde\Xi}\tilde\Pi_+=\tilde\Pi_+,\qquad L_{\tilde\Xi}\vec\Upsilon_+=-\vec\Upsilon_+,
$$

and in the couple $\mathcal{C}_-$,

$$
L_{\tilde\Xi}\vec\Upsilon_-=\vec\Upsilon_-,\qquad L_{\tilde\Xi}\tilde\Pi_-=-\tilde\Pi_- .
$$

In each couple the matrix is $\operatorname{diag}(1,-1)$. The **half-root** $\tfrac12\tilde\Xi$ therefore has the weights $+\tfrac12,-\tfrac12$ on each plane, and the highest weight is $\tfrac12$: each spinor space is a spin-$\tfrac12$ carrier.

**Chirality versus spin weight.** The right action of the same root is scalar on each plane: $R_{\tilde\Xi}=+1$ on $S_+$ and $R_{\tilde\Xi}=-1$ on $S_-$, because $\tilde\Pi_+\tilde\Xi=\tilde\Pi_+$ and $\vec\Upsilon_+\tilde\Xi=\vec\Upsilon_+$, while $\vec\Upsilon_-\tilde\Xi=-\vec\Upsilon_-$ and $\tilde\Pi_-\tilde\Xi=-\tilde\Pi_-$. The eigenvalue of $R_{\tilde\Xi}$ is the **chirality**, the eigenvalue of $L_{\tilde\Xi}$ is the **spin weight**. The two planes have the same spin weights and opposite chirality; the two words are independent, and the identity $L_{\tilde\Xi}=\operatorname{ad}_{\tilde\Xi}+R_{\tilde\Xi}$ reads the spin weight as the sum of the commutator weight and the chirality.

**The ladder.** The two nilpotents act by left multiplication as the ladder of the plane. In each couple,

$$
L_{\vec\Upsilon_-}=\begin{pmatrix}0&1\\0&0\end{pmatrix},
\qquad
L_{\vec\Upsilon_+}=\begin{pmatrix}0&0\\1&0\end{pmatrix},
$$

because the left action is the Peirce matrix $\mathsf M(\tilde P)$ in both couples. The operator $\vec\Upsilon_-$ raises the weight by one and $\vec\Upsilon_+$ lowers it by one; in $\mathcal{C}_-$ the two basis vectors exchange their roles, and the two matrices are unchanged.

**The triple.** The three elements $\tfrac12\tilde\Xi$, $E=\vec\Upsilon_-$ and $F=\vec\Upsilon_+$ satisfy

$$
[H,E]=E,\qquad [H,F]=-F,\qquad [E,F]=2H .
$$

The spin-$\tfrac12$ of each plane is the Peirce frame read as an $\mathfrak{sl}_2$ triple. The proof, the vector carrier, the projectors and the half-angle are in *The Spin of a Biquaternion*.

## The Right Action

**Right multiplication is the operation that relates the two spinor spaces: it preserves one of them only under a condition on the Peirce matrix, and it exchanges them through the mixed units.**

Right multiplication by $\tilde P$ sends

$$
\tilde\Pi_+\longmapsto p_{11}\tilde\Pi_++p_{12}\vec\Upsilon_-,
\qquad
\vec\Upsilon_+\longmapsto p_{11}\vec\Upsilon_++p_{12}\tilde\Pi_-,
$$

so it preserves $S_+$ exactly when $p_{12}=0$; it sends

$$
\vec\Upsilon_-\longmapsto p_{21}\tilde\Pi_++p_{22}\vec\Upsilon_-,
\qquad
\tilde\Pi_-\longmapsto p_{21}\vec\Upsilon_++p_{22}\tilde\Pi_-,
$$

so it preserves $S_-$ exactly when $p_{21}=0$. When both entries vanish, $\tilde P$ is diagonal and right multiplication acts by the scalar $p_{11}$ on $S_+$ and $p_{22}$ on $S_-$. In general the right action mixes the two chiralities, whereas the left action never does.

**The exchange.** Right multiplication by the mixed unit $\vec\Upsilon_-$ carries $S_+$ to $S_-$, and right multiplication by $\vec\Upsilon_+$ carries $S_-$ to $S_+$:

$$
S_+\longrightarrow S_-,\quad\xi\longmapsto\xi\vec\Upsilon_-,
\qquad
S_-\longrightarrow S_+,\quad\eta\longmapsto\eta\vec\Upsilon_+ .
$$

The two maps are inverse, because for $\xi\in S_+$ and $\eta\in S_-$

$$
(\xi\vec\Upsilon_-)\vec\Upsilon_+=\xi(\vec\Upsilon_-\vec\Upsilon_+)=\xi\tilde\Pi_+=\xi,
\qquad
(\eta\vec\Upsilon_+)\vec\Upsilon_-=\eta(\vec\Upsilon_+\vec\Upsilon_-)=\eta\tilde\Pi_-=\eta .
$$

So the two spinor spaces are exchanged by a pair of mutually inverse bijections. The exchange is not canonical: the normalisation of the mixed basis is free up to the reciprocal rescaling $\vec\Upsilon_-\mapsto\mu\vec\Upsilon_-$, $\vec\Upsilon_+\mapsto\mu^{-1}\vec\Upsilon_+$ of §*Systems of Matrix Units* of *The Peirce Decomposition*, which leaves every product and the frame unchanged and conjugates the exchange.

The exchange is a bijection of two subspaces. It is neither a left multiplication nor an algebra automorphism; it is the concrete form of the statement that the two spinor spaces are the same object in two copies.

## The Star

**The star carries a spinor space to a right Peirce row, not to the other spinor space; chirality belongs to the left grouping, not to the Hermitian structure.**

The star acts on the subspace generated on the left by an idempotent by

$$
S_+^{*}=(\mathbb{B}\tilde\Pi_+)^{*}=\tilde\Pi_+^{*}\mathbb{B}.
$$

For the Hermitian pair $\tilde\Pi_+^{*}=\tilde\Pi_+$, so $S_+^{*}=\tilde\Pi_+\mathbb{B}=\mathbb{C}\tilde\Pi_+\oplus\mathbb{C}\vec\Upsilon_-$, the right Peirce row of the same idempotent. It is not $S_-$ and it is not a spinor space: the two spinor spaces are planes closed on the left, while $S_+^{*}$ is a plane closed on the right. The image is the transpose of a spinor space, a different subspace of the algebra. The spinor adjoints and the reality conditions are treated in *Peirce Carriers and Inner Conjugation* and *Real Spinors and Reality Conditions on the Biquaternion Algebra with Hermitian Adjoint*.

## The Matrix Picture

**In the $M_2(\mathbb{C})$ Peirce model the two spinor spaces are the two columns, left multiplication multiplies a column, and right multiplication multiplies the matrix and mixes the columns.**

Under the coordinate isomorphism of §*The Peirce Coordinates and the Matrix Model* of *The Peirce Decomposition*, the basis $\mathcal{C}_+$ becomes the first column and $\mathcal{C}_-$ the second:

$$
S_+\longmapsto\mathbb{C}E_{11}\oplus\mathbb{C}E_{21},
\qquad
S_-\longmapsto\mathbb{C}E_{12}\oplus\mathbb{C}E_{22}.
$$

The representative of a spinor of first chirality is a column vector, and the left action of $\tilde P$ is multiplication of that column by $\mathsf M(\tilde P)$. The right action multiplies the whole matrix on the right and therefore mixes the two columns. The matrix form is *$M_2(\mathbb{C})$ Model : Peirce Coordinates, Matrix Units and the Spinor Planes*.

## Summary

- The Peirce frame carries two planes $S_+=\mathbb{B}\tilde\Pi_+$ and $S_-=\mathbb{B}\tilde\Pi_-$, the spinor spaces, with $\mathbb{B}=S_+\oplus S_-$ as a vector space.
- Each plane is spanned by a couple $\mathcal{C}_\pm$ made of one idempotent and one nilpotent.
- Left multiplication preserves each plane and acts on both by the same Peirce matrix $\mathsf M(\tilde P)$.
- The root $\tilde\Xi$ has left weights $+1,-1$ in each couple; the half-root $\tfrac12\tilde\Xi$ has weights $\pm\tfrac12$, so each plane is a spin-$\tfrac12$ carrier.
- The right root is the chirality scalar, $+1$ on $S_+$ and $-1$ on $S_-$; chirality and spin weight are independent.
- The nilpotents $\vec\Upsilon_-,\vec\Upsilon_+$ are the raising and lowering operators in both couples, and $\tfrac12\tilde\Xi,\vec\Upsilon_-,\vec\Upsilon_+$ form an $\mathfrak{sl}_2$ triple.
- Right multiplication exchanges the two planes through the mixed units; the exchange is a pair of inverse bijections, canonical only up to the rescaling of the mixed basis.
- The star carries $S_+$ to the right Peirce row $\tilde\Pi_+\mathbb{B}$, not to $S_-$.
- Nothing in the article uses a form, a norm or a module.

## Summary of Notation

| symbol | meaning |
|---|---|
| $S_\pm=\mathbb{B}\tilde\Pi_\pm$ | the two spinor spaces |
| $\mathcal{C}_+=(\tilde\Pi_+,\vec\Upsilon_+)$, $\mathcal{C}_-=(\vec\Upsilon_-,\tilde\Pi_-)$ | the two couples, bases of the spinor spaces |
| $\vec\Upsilon_-\in\mathbb{B}_{+-}$, $\vec\Upsilon_+\in\mathbb{B}_{-+}$ | the mixed Peirce units |
| $\tilde\Xi=\tilde\Pi_+-\tilde\Pi_-$ | the frame root |
| $\tfrac12\tilde\Xi$ | the half-root, the spin operator when $\tilde\Xi$ is Hermitian |
| $\mathsf M(\tilde P)$ | the Peirce matrix of $\tilde P$ |

## Further Reading

- [The Peirce Decomposition](ideals-peirce-decompositions-and-spinors-in-the-biquaternion-algebra.html), for the corners, the Peirce table, the mixed units and the weight table.
- [The Spin of a Biquaternion](the-spin-of-a-biquaternion.html), for the triple, the vector carrier, the projectors and the half-angle.
- [The Minimal Left Ideals](the-minimal-left-ideals.html), for the module reading of the two spaces.
- [$M_2(\mathbb{C})$ Model : Peirce Coordinates, Matrix Units and the Spinor Planes](m2c-representation-the-peirce-coordinates-matrix-units-and-the-spinor-planes.html), for the matrix picture.
- [Peirce Carriers and Inner Conjugation](peirce-carriers-and-inner-conjugation.html), for the adjoints and the reality conditions.
