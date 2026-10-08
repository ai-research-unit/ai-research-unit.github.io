
# __The Complex Bilinear Form on the Biquaternion Algebra__

## Introduction

The biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ carries four scalar forms, one to each of the four products of *The Four Biquaternion Complex Products*, and this article is the entry point of the reading group that develops the first of them. The **complex bilinear form** is the scalar part of the plain product,

$$
\langle\tilde P,\tilde Q\rangle=\mathrm{Sc}(\tilde P\tilde Q)=\sum_{\mu=0}^{3}\varepsilon_\mu P_\mu Q_\mu,\qquad \varepsilon=(1,-1,-1,-1).
$$

No conjugation enters either argument, so the form is $\mathbb{C}$-linear in each of them; it is symmetric, non-degenerate and indefinite, with Gram matrix $D=\operatorname{diag}(1,-1,-1,-1)$ in the coefficient basis. Its diagonal $\langle\tilde Q,\tilde Q\rangle=\sum_\mu\varepsilon_\mu Q_\mu^2$ is the quadratic form it polarises, and the diagonal singles out the two subsets this group develops — the null quadric and the level set — together with the group of complex-linear maps that preserve the form.

The article is the entry point of the group. It defines the form and fixes its matrices; it develops the null quadric, the level set and the isometry group $O_4(\mathbb{C})$. The restriction of the form to the six distinguished real subspaces is *The Six Subspaces under the Complex Bilinear Form*; the transpose the form defines on the linear operators is *Association and the Transpose on the Biquaternion Algebra*, and the comparison with the three other forms of the algebra is *The Four Pairings of the Biquaternion Algebra*.

Two warnings fix the boundary of the group. First, the form must not be confused with the **quaternion bilinear form** $\langle\tilde P,\tilde Q\rangle_{\natural}=\mathrm{Sc}(\tilde P\tilde Q^{\natural})=\sum_\mu P_\mu Q_\mu$ of *The Quaternion Bilinear Form on the Biquaternion Algebra*: the two differ by the sign vector $\varepsilon$ alone, they share the isometry group $O_4(\mathbb{C})$ and the realified signature $(4,4)$, and they are nevertheless different pairings, of Gram matrices $D$ and $\mathrm{I}_4$. The whole of the resemblance and the whole of the distinction are in those two matrices. Second, the null quadric of the complex bilinear form is not the null cone of the zero divisors: the latter is the zero set of the quaternion bilinear diagonal $\sum_\mu Q_\mu^2$, and the two complex cones must not be identified.

The article assumes the algebra, its basis and its conjugations from *Biquaternions as a Vector Space over $\mathbb{C}$*, the four products from *The Four Biquaternion Complex Products*, the six subspaces from *Introduction to the Six Subspaces*, and the general theory of bilinear and quadratic forms from *Bilinear Forms* and *Quadratic Forms and Polarisation*.

## The Form and Its Polarisation

**Definition.** The **complex bilinear form** is the scalar part of the plain product,

$$
\langle\tilde P,\tilde Q\rangle=\mathrm{Sc}(\tilde P\tilde Q),\qquad \tilde P,\tilde Q\in\mathbb{B}.
$$

On the coordinates $\tilde P=\sum_\mu P_\mu e_\mu$ and $\tilde Q=\sum_\mu Q_\mu e_\mu$ the scalar part of the product is read from $\mathrm{Sc}(e_\mu e_\nu)=\varepsilon_\mu\delta_{\mu\nu}$, so that

$$
\langle\tilde P,\tilde Q\rangle=\sum_{\mu=0}^{3}\varepsilon_\mu P_\mu Q_\mu=P_0Q_0-P_1Q_1-P_2Q_2-P_3Q_3.
$$

**Proposition (bilinearity, symmetry, non-degeneracy).** The form is $\mathbb{C}$-bilinear, symmetric and non-degenerate.

*Proof.* Bilinearity is the bilinearity of the product in each factor together with the linearity of the scalar part; symmetry is the symmetry of the coefficient expression; and non-degeneracy is the invertibility of the Gram matrix $D$, whose determinant is $-1$, computed in the next section.

**Proposition (the diagonal and the polarisation).** The quadratic form of the form is

$$
\langle\tilde Q,\tilde Q\rangle=\sum_{\mu=0}^{3}\varepsilon_\mu Q_\mu^2=Q_0^2-Q_1^2-Q_2^2-Q_3^2,
$$

and the form is its polar form,

$$
\langle\tilde P,\tilde Q\rangle=\tfrac{1}{2}\Bigl(\langle\tilde P+\tilde Q,\tilde P+\tilde Q\rangle-\langle\tilde P,\tilde P\rangle-\langle\tilde Q,\tilde Q\rangle\Bigr).
$$

*Proof.* Substituting $\tilde P=\tilde Q$ gives the first display, and the polarisation identity is the standard recovery of a symmetric bilinear form from its diagonal over a field of characteristic different from two (*Quadratic Forms and Polarisation*, §*The Polar Form*).

**Remark (the diagonal is not a norm).** The diagonal takes both signs, $\langle e_0,e_0\rangle=1$ against $\langle e_1,e_1\rangle=-1$, so the form is indefinite and its diagonal is not a norm; the length it can supply comes from a symmetry of the form and not from the diagonal, by the argument of *Biquaternion Forms and Algebraic Norms*, §*Distances Read from the Forms*. The same warning separates the two bilinear forms: the diagonal of the complex bilinear form is $\sum_\mu\varepsilon_\mu Q_\mu^2$, the diagonal of the quaternion bilinear form is the norm $\sum_\mu Q_\mu^2$.

## The Gram Matrix and the Realification

**Definition.** The **Gram matrix** of the form in the coefficient basis is the sign matrix

$$
G_{ij}=\langle e_i,e_j\rangle=\varepsilon_i\,\delta_{ij},\qquad G=\operatorname{diag}(1,-1,-1,-1)=D.
$$

It is symmetric, as a bilinear form must be; it is invertible, of determinant $\det D=-1$, so the form is non-degenerate; and its inertia over the reals is $(1,3)$, the positive direction being $e_0$ and the negative directions $e_1,e_2,e_3$. This is the whole of the inertia of the coefficient basis.

**Proposition (congruence and uniqueness over $\mathbb{C}$).** Under a change of basis with matrix $S$ the Gram matrix becomes $S^{\mathsf T}DS$. Two forms are isometric exactly when their Gram matrices are congruent, so the rank and the discriminant are invariants of the isometry class. Over $\mathbb{C}$ every non-degenerate symmetric form of rank $4$ is congruent to $D$, and the complex bilinear form is therefore the unique non-degenerate symmetric form on $\mathbb{C}^4$ up to linear isometry.

*Proof.* The Gram matrix in the new basis is $S^{\mathsf T}DS$ by bilinearity; congruence preserves the rank and multiplies the determinant by $(\det S)^2$, so the rank and the discriminant, the determinant modulo squares, are the invariants of the isometry class (*Bilinear Forms*, §*Congruence and the Discriminant*). Over $\mathbb{C}$, where every non-zero scalar is a square, the discriminant is trivial and the classification of non-degenerate symmetric forms is by the rank alone; the determinant of a rank-$4$ form can be normalised to $1$. Verified: the diagonal change of basis $\operatorname{diag}(1,i,i,i)$ carries $D$ to the orthogonal form $\mathrm{I}_4$, so the two are isometric over $\mathbb{C}$; their isometry groups are conjugate, which is why the two bilinear forms of the algebra share $O_4(\mathbb{C})$.

**Proposition (the realification).** Write a biquaternion on the eight real basis elements $(e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3)$ as $\tilde Q=\sum_\mu q_\mu e_\mu+\sum_\mu q'_\mu\,ie_\mu$ with $q_\mu,q'_\mu\in\mathbb{R}$. The realified form is the real symmetric form of Gram matrix

$$
\operatorname{diag}(D,-D)=\operatorname{diag}(1,-1,-1,-1,-1,1,1,1),
$$

of signature $(4,4)$.

*Proof.* Because the form is $\mathbb{C}$-bilinear, its values on the real basis are read from $\mathrm{Sc}(e_\mu e_\nu)=\varepsilon_\mu\delta_{\mu\nu}$ and the centrality of $i$,

$$
\langle e_\mu,e_\nu\rangle=\varepsilon_\mu\delta_{\mu\nu},\qquad
\langle e_\mu,ie_\nu\rangle=i\,\varepsilon_\mu\delta_{\mu\nu},\qquad
\langle ie_\mu,ie_\nu\rangle=-\varepsilon_\mu\delta_{\mu\nu}.
$$

The middle entries are purely imaginary, so they do not contribute to the real part of the form, which is the realified symmetric form; the remaining entries are $\varepsilon_\mu\delta_{\mu\nu}$ on the first four basis elements and $-\varepsilon_\mu\delta_{\mu\nu}$ on the last four. The two blocks have opposite sign and four entries each, giving the signature $(4,4)$. Verified on the $8\times8$ real Gram matrix, whose eigenvalues are four $+1$ and four $-1$.

**Remark (the sign flip is the complex structure).** The passage from the block $D$ to the block $-D$ is the realification of the central scalar: a complex bilinear form reads $+1$ on a real direction and $-1$ on the same direction multiplied by $i$, since $\langle i\tilde P,i\tilde Q\rangle=-\langle\tilde P,\tilde Q\rangle$. The realified form is therefore split, of signature $(4,4)$, although the diagonal $\sum_\mu\varepsilon_\mu Q_\mu^2$ is a complex quadratic form and has no signature until a real form is chosen.

**Remark (the central scalar is an anti-isometry).** Multiplication by $i$ reverses the form, $\langle i\tilde P,i\tilde Q\rangle=-\langle\tilde P,\tilde Q\rangle$, so the central scalar is an anti-isometry and not an isometry; it exchanges the block $D$ with the block $-D$ in the realified matrix, hence the split signature, and it exchanges the positive definite Hermitian subspace with the negative definite anti-Hermitian one.

## The Null Quadric

**Definition.** The **null quadric** of the form is its zero set,

$$
\mathcal{Q}=\Bigl\{\tilde Q\in\mathbb{B}:\langle\tilde Q,\tilde Q\rangle=\sum_{\mu=0}^{3}\varepsilon_\mu Q_\mu^2=0\Bigr\}.
$$

**Proposition (dimension and smoothness).** The null quadric is a complex quadric hypersurface of complex dimension $3$ and real dimension $6$. It is smooth of real dimension $6$ away from the apex $\tilde Q=0$, and the apex is its only singular point.

*Proof.* On $\mathbb{B}\cong\mathbb{C}^4$ the condition is the vanishing of the polynomial $f(Q_0,\dots,Q_3)=\sum_\mu\varepsilon_\mu Q_\mu^2$, whose gradient is $\nabla f=2(\varepsilon_0 Q_0,\dots,\varepsilon_3 Q_3)$; the gradient is non-zero exactly off the apex, so the complex hypersurface is smooth there, of complex dimension $3$ and real dimension $6$. At the apex all four complex partial derivatives vanish, so the apex is singular. Equivalently, $f$ gives the two real equations $\mathrm{Re}\,f=0$ and $\mathrm{Im}\,f=0$, whose real Jacobian has rank $2$ exactly off the apex. Verified on random points of $\mathcal{Q}$ and at the apex: the rank is $2$ off the apex and $0$ at it.

**Proposition (rulings and isotropic planes).** The null quadric is ruled. It carries two families of **isotropic planes**, each of complex dimension $2$ and real dimension $4$, on which the form vanishes identically; through each smooth point of the quadric pass two such planes, one from each family. For example

$$
W_{+}=\mathrm{span}_{\mathbb{C}}\{e_0+e_1,\;e_2+ie_3\},\qquad
W_{-}=\mathrm{span}_{\mathbb{C}}\{e_0-e_1,\;e_2-ie_3\}
$$

are totally isotropic, and the maximal dimension of a totally isotropic subspace of the complex bilinear form is $2$ over $\mathbb{C}$, that is $4$ over $\mathbb{R}$.

*Proof.* On the generators of $W_{+}$ the form vanishes, $\langle e_0+e_1,e_0+e_1\rangle=1-1=0$, $\langle e_2+ie_3,e_2+ie_3\rangle=-1+i^2(-1)=-1+1=0$ and $\langle e_0+e_1,e_2+ie_3\rangle=0$, and the same computation holds for $W_{-}$; a $\mathbb{C}$-bilinear form vanishing on a generating set vanishes on the span, so both planes are totally isotropic. The upper bound is the Witt index: over $\mathbb{C}$ every non-degenerate symmetric form of rank $4$ is equivalent to the hyperbolic form, whose maximal totally isotropic dimension is $2$, and the two planes above attain it. The realified form, of signature $(4,4)$, has maximal totally isotropic real dimension $\min(4,4)=4$ over $\mathbb{R}$, attained for instance by $\operatorname{span}_{\mathbb{R}}\{e_0+e_1,\;ie_1+e_2,\;ie_2+e_3,\;ie_3+ie_0\}$. Verified: the form vanishes on $W_+$ and on $W_-$, and on the four real generators of the last span.

**Proposition (the form is hyperbolic over $\mathbb{C}$).** The form is an orthogonal sum of two hyperbolic planes. The four elements

$$
h_1=e_0+e_1,\qquad h_2=\tfrac{1}{2}(e_0-e_1),\qquad h_3=e_2+ie_3,\qquad h_4=\tfrac{1}{2}(ie_3-e_2)
$$

are isotropic, $\langle h_i,h_i\rangle=0$; the only non-zero pairings among them are $\langle h_1,h_2\rangle=1$ and $\langle h_3,h_4\rangle=1$; and the Gram matrix in this basis is

$$
\begin{pmatrix}0&1&0&0\\1&0&0&0\\0&0&0&1\\0&0&1&0\end{pmatrix}.
$$

*Proof.* Direct substitution using $\langle e_i,e_j\rangle=\varepsilon_i\delta_{ij}$: $\langle h_1,h_1\rangle=\varepsilon_0+\varepsilon_1=0$, $\langle h_2,h_2\rangle=\tfrac14(\varepsilon_0+\varepsilon_1)=0$ and $\langle h_1,h_2\rangle=\tfrac12(\varepsilon_0-\varepsilon_1)=1$; similarly $\langle h_3,h_3\rangle=\varepsilon_2-\varepsilon_3=0$, $\langle h_4,h_4\rangle=\tfrac14(\varepsilon_2-\varepsilon_3)=0$ and $\langle h_3,h_4\rangle=\tfrac12(-\varepsilon_2-\varepsilon_3)=1$; the pairings between the plane of $\{h_1,h_2\}$ and the plane of $\{h_3,h_4\}$ vanish because the two planes are spanned by disjoint units. Verified numerically on all sixteen pairings.

**Remark (the hyperbolic splitting and the Witt index).** The two hyperbolic planes of the basis are $\mathrm{span}\{h_1,h_2\}=\mathrm{span}\{e_0,e_1\}$ and $\mathrm{span}\{h_3,h_4\}=\mathrm{span}\{e_2,e_3\}$; each is non-degenerate of signature $(1,1)$ over the reals, the two are orthogonal to each other, and each contains exactly its two isotropic lines. The maximal totally isotropic dimension of a hyperbolic plane is $1$, and the index is additive over orthogonal sums, so the index of the form is $1+1=2$, in agreement with the Witt-index computation above.

**Remark (the quadric is an affine cone over a smooth projective quadric).** The defining polynomial is homogeneous, $f(t\tilde Q)=t^2f(\tilde Q)$ for $t\in\mathbb{C}$, so the null quadric is a complex cone with apex the origin: it is the affine cone over the projective quadric surface

$$
\bigl\{[Q_0:Q_1:Q_2:Q_3]\in\mathbb{P}^3:\textstyle\sum_\mu\varepsilon_\mu Q_\mu^2=0\bigr\}.
$$

The projective quadric is smooth, because the form is non-degenerate, and it is the ruled quadric surface whose two families of projective lines are the rulings of the previous proposition. The apex of the affine cone is the singularity recorded above, and every point of the quadric lies on a complex line through the apex.

**Remark (the quadric is not the zero-divisor cone).** The null quadric $\mathcal{Q}$ is the zero set of $\sum_\mu\varepsilon_\mu Q_\mu^2$, whereas the **null cone** of the algebra is the zero set of the quaternion bilinear diagonal $\sum_\mu Q_\mu^2$, whose non-zero elements are the zero divisors. The two complex cones are distinct. The element $e_0+e_1$ lies on $\mathcal{Q}$ and not on the zero-divisor cone, since $1-1=0$ while $1+1=2$; the element $e_0+ie_1$ lies on the zero-divisor cone and not on $\mathcal{Q}$, since $1+i^2=0$ while $1-i^2=2$; and the element $e_1+ie_2$ lies on both, since $1+i^2=0$ and $-1-(-1)=0$. The companion cone is *The Isotropic Structure of the Quaternion Bilinear Form*.

## The Level Set

**Definition.** The **level set** of the form at one is

$$
\mathcal{L}=\Bigl\{\tilde Q\in\mathbb{B}:\sum_{\mu=0}^{3}\varepsilon_\mu Q_\mu^2=1\Bigr\}.
$$

**Proposition (a non-compact complex quadric of real dimension $6$).** The level set is a smooth affine complex quadric of complex dimension $3$ and real dimension $6$, and it is non-compact.

*Proof.* The defining polynomial $f-1$ has the same gradient as $f$, non-zero at every point of $\mathcal{L}$ since $\mathcal{L}$ avoids the apex, so $\mathcal{L}$ is a smooth complex hypersurface of complex dimension $3$ and real dimension $6$. At $\tilde Q=e_0$ the real Jacobian of $(\mathrm{Re}\,f,\mathrm{Im}\,f)$ has rank $2$, confirming the dimension by the implicit function theorem. For non-compactness, the real curve $\tilde Q(t)=\cosh t\,e_0+\sinh t\,e_1$, $t\in\mathbb{R}$, satisfies $\cosh^2 t-\sinh^2 t=1$ and is unbounded. Verified: the rank at $e_0$ is $2$ and the curve lies on $\mathcal{L}$.

**Remark (the level set is not a group).** Multiplicativity fails: with $\tilde Q(t)=\cosh t\,e_0+\sinh t\,e_1$ one has $\langle\tilde Q(t),\tilde Q(t)\rangle=1$ while $\tilde Q(t)^2=e_0+\sinh 2t\,e_1$, of diagonal value $1-\sinh^2 2t$, which differs from $1$ for $t\neq0$. The level set is therefore not closed under the product and is not a group. This separates it from the level set of the quaternion bilinear form, which is the norm-one group $G_1$ of *Biquaternion Norm and Invertibility*.

**Remark (the level set is a complex quadric).** Over $\mathbb{C}$ all non-degenerate quadratic forms of rank $4$ are equivalent, so the affine quadric $\mathcal{L}$ is the standard complex quadric of real dimension $6$, the complex analogue of the hyperboloid of a real form of signature $(1,3)$. Its place among the four level sets of the algebra is the table of *Biquaternion Forms and Algebraic Norms*, §*The Geometry: Null Sets, Level Sets and Isometry Groups*.

## The Isometry Group

**Definition.** An **isometry** of the form is a $\mathbb{C}$-linear map $T$ of $\mathbb{B}$ preserving it,

$$
\langle T\tilde P,T\tilde Q\rangle=\langle\tilde P,\tilde Q\rangle\qquad\text{for all }\tilde P,\tilde Q\in\mathbb{B}.
$$

**Theorem (the isometry group).** In the coefficient basis the isometry group is

$$
\mathrm{Isom}\bigl(\langle\cdot,\cdot\rangle\bigr)=\{T\in GL_4(\mathbb{C}):T^{\mathsf T}DT=D\}=O_4(\mathbb{C}),
$$

of complex dimension $6$ and real dimension $12$, and it is non-compact. It is the same group as the isometry group of the quaternion bilinear form.

*Proof.* A $\mathbb{C}$-linear $T$ preserves the form exactly when $T^{\mathsf T}DT=D$, since the Gram matrix of the form on the two images is $T^{\mathsf T}DT$; the group so defined is the complex orthogonal group of the sign matrix. Its Lie algebra is $\{X:X^{\mathsf T}D+DX=0\}$, which is the space of antisymmetric complex $4\times4$ matrices under $X\mapsto DX$, of complex dimension $6$, hence real dimension $12$. The group is non-compact because it contains the hyperbolic rotation of the plane $\mathbb{R}\{e_0,e_1\}$, $e_0\mapsto\cosh u\,e_0+\sinh u\,e_1$ and $e_1\mapsto\sinh u\,e_0+\cosh u\,e_1$ with $e_2,e_3$ fixed, for every $u$. The same computation with Gram matrix $\mathrm{I}_4$ gives the isometry group of the quaternion bilinear form, $\{T:T^{\mathsf T}T=\mathrm{I}_4\}$, which is $O_4(\mathbb{C})$ as well. Verified: the real linear system $X^{\mathsf T}D+DX=0$ has $32$ unknowns and rank $20$, so its solution space has real dimension $12$.

**Proposition (the real forms).** The real structures of the algebra exhibit the real forms of $O_4(\mathbb{C})$. The Hermitian conjugation ${}^{*}$ is an antilinear isometry, $\langle\tilde P^{*},\tilde Q^{*}\rangle=\overline{\langle\tilde P,\tilde Q\rangle}$, with fixed space the Hermitian subspace $\mathbb{M}_+$, of restriction signature $(4,0)$; the $\mathbb{C}$-linear isometries commuting with ${}^{*}$ form the compact real orthogonal group $O(4)$, of real dimension $6$. The complex conjugation is an antilinear isometry of the same kind, with fixed space the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, of restriction signature $(1,3)$; the $\mathbb{C}$-linear isometries commuting with it form the real orthogonal group $O(1,3)$, of real dimension $6$. The conjugate real structure, with fixed space the anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$ of signature $(3,1)$, exhibits the isomorphic group $O(3,1)$.

*Proof.* In coordinates $(\tilde P^{*})_\mu=\varepsilon_\mu\overline{P_\mu}$ and $(\bar{\tilde P})_\mu=\overline{P_\mu}$. The outer sign of the form then gives $\langle\tilde P^{*},\tilde Q^{*}\rangle=\sum_\mu\varepsilon_\mu\,(\varepsilon_\mu\overline{P_\mu})(\varepsilon_\mu\overline{Q_\mu})=\sum_\mu\varepsilon_\mu^3\overline{P_\mu Q_\mu}=\sum_\mu\varepsilon_\mu\overline{P_\mu Q_\mu}$, since $\varepsilon_\mu^3=\varepsilon_\mu$ for $\varepsilon_\mu\in\{1,-1\}$, and $\langle\bar{\tilde P},\bar{\tilde Q}\rangle=\sum_\mu\varepsilon_\mu\overline{P_\mu Q_\mu}$ as well; both sums are $\overline{\langle\tilde P,\tilde Q\rangle}$. The fixed space of ${}^{*}$ is the Hermitian subspace and that of the complex conjugation is the quaternion subspace, of restriction signatures $(4,0)$ and $(1,3)$ (*The Six Subspaces under the Complex Bilinear Form*); a $\mathbb{C}$-linear map commuting with an antilinear involution is the complexification of a real map on the fixed space, and it preserves the form exactly when the real map does. Both real groups have real dimension $n(n-1)/2=6$. Verified on the realified restriction Gram matrices.

**Remark (which subspace exhibits which real form).** The Hermitian subspace is positive definite of signature $(4,0)$, so the real form of the isometry group it exhibits is the compact $O(4)$; the quaternion subspace is of signature $(1,3)$, so the real form it exhibits is $O(1,3)$, and the anti-quaternion subspace exhibits the isomorphic $O(3,1)$. The two are the two real forms of the same complex group $O_4(\mathbb{C})$, and they are separated by the choice of real structure, the Hermitian conjugation ${}^{*}$ against the complex conjugation. The natural conjugation ${}^{\natural}$ is a $\mathbb{C}$-linear isometry and is not a real structure: it fixes only the scalar line $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$, and it is the map that transports the complex bilinear form to the quaternion bilinear form, as the transport remark below records.

**Remark (the complex isometry group is not the real one).** The isometry group here is the group of $\mathbb{C}$-linear isometries. The group of *real-linear* isometries of the realified form is the larger $O(4,4)$, of real dimension $28$, and it is not the subject of this article; the group $O_4(\mathbb{C})$ is the group the form defines over $\mathbb{C}$.

**Remark (the transport to the sibling bilinear form).** The natural conjugation is a $\mathbb{C}$-linear isometry carrying this form to the quaternion bilinear form of *The Quaternion Bilinear Form on the Biquaternion Algebra*:

$$
\langle\tilde P^{\natural},\tilde Q\rangle=\sum_\mu\varepsilon_\mu^2 P_\mu Q_\mu=\sum_\mu P_\mu Q_\mu=\langle\tilde P,\tilde Q\rangle_{\natural}.
$$

The map carries the complex bilinear form to the quaternion bilinear form, and the whole difference of the two is the sign vector $\varepsilon$ that it absorbs in the first argument. The four forms side by side, their Gram matrices and their isometry groups are *The Four Pairings of the Biquaternion Algebra*.

## Worked Examples

The form is evaluated on a few elements that recur in the group.

**The units.** The form is diagonal on the coefficient basis, $\langle e_0,e_0\rangle=1$ and $\langle e_k,e_k\rangle=-1$ for $k=1,2,3$, with every cross entry zero. Two mixed elements follow from the diagonal: $\langle e_0+e_1,e_0+e_1\rangle=1-1=0$ and $\langle e_0+ie_1,e_0+ie_1\rangle=1-i^2=2$.

**The two cones crossed.** The element $e_1+ie_2$ is null, $\langle e_1+ie_2,e_1+ie_2\rangle=-1-(-1)=0$, and it is a zero divisor as well, since it lies on both complex cones; the element $e_0+e_1$ is null and is not a zero divisor; and the element $e_0+ie_1$ is a zero divisor and is not null. The three together separate the null quadric of this form from the zero-divisor cone of *The Isotropic Structure of the Quaternion Bilinear Form*, and the two cones meet in the pure cone of *The Realification of the Four Forms*.

**The Hermitian sector is positive definite.** For real $a,b$ the element $a e_0+b\,ie_1$ has diagonal value $a^2+b^2$, positive off zero, and the computation generalises to the whole Hermitian subspace: the restriction there is positive definite of signature $(4,0)$, and the anti-Hermitian subspace is negative definite because the form changes sign under multiplication by $i$.

**The polarisation on an orthogonal pair.** For the pair $e_0,e_1$ the polarisation identity gives $\langle e_0,e_1\rangle=\tfrac12(\langle e_0+e_1,e_0+e_1\rangle-\langle e_0,e_0\rangle-\langle e_1,e_1\rangle)=\tfrac12(0-1+1)=0$, the diagonal expression of the vanishing off-diagonal entry.

**An isometry.** The hyperbolic rotation of the plane $\mathbb{R}\{e_0,e_1\}$, with $T e_0=\cosh u\,e_0+\sinh u\,e_1$, $T e_1=\sinh u\,e_0+\cosh u\,e_1$ and $T e_2=e_2$, $T e_3=e_3$, preserves the form for every real $u$; it is the element of $O_4(\mathbb{C})$ that makes the isometry group non-compact.

**The centre and its null lines.** On the centre the restriction is $q_0^2-(q'_0)^2$, null exactly on the two real lines $\mathbb{R}(e_0\pm ie_0)$; the centre is the hyperbolic plane of signature $(1,1)$ in the restriction table, and its two null directions are the two isotropic lines of that plane.

**The isotropic plane $W_+$.** The elements $\tilde Q=a(e_0+e_1)+b(e_2+ie_3)$ with $a,b\in\mathbb{C}$ are all null, and they are the isotropic plane $W_+$ of the null-quadric section. A plane of the other ruling is $\mathrm{span}\{e_0+e_1,e_2-ie_3\}$, which meets $W_+$ in the line $\mathbb{C}(e_0+e_1)$ and is totally isotropic, since $\langle e_0+e_1,e_2-ie_3\rangle=0$ and $\langle e_2-ie_3,e_2-ie_3\rangle=-1-(-1)=0$.

## Summary

The **complex bilinear form** of the biquaternion algebra is $\langle\tilde P,\tilde Q\rangle=\mathrm{Sc}(\tilde P\tilde Q)=\sum_\mu\varepsilon_\mu P_\mu Q_\mu$ with $\varepsilon=(1,-1,-1,-1)$; it is $\mathbb{C}$-bilinear, symmetric and non-degenerate, of Gram matrix $D=\operatorname{diag}(1,-1,-1,-1)$, of determinant $-1$ and inertia $(1,3)$, and of realified Gram matrix $\operatorname{diag}(D,-D)$ of signature $(4,4)$. Its diagonal is the quadratic form $\sum_\mu\varepsilon_\mu Q_\mu^2$, which it polarises. Its null quadric $\sum_\mu\varepsilon_\mu Q_\mu^2=0$ is a complex quadric of real dimension $6$, smooth away from the apex, ruled by two families of totally isotropic planes of complex dimension $2$; the maximal totally isotropic dimension is $2$ over $\mathbb{C}$ and $4$ over $\mathbb{R}$, and the quadric is not the zero-divisor cone. Its level set $\sum_\mu\varepsilon_\mu Q_\mu^2=1$ is a non-compact complex quadric of real dimension $6$, and it is not a group. Its isometry group is $O_4(\mathbb{C})$, of complex dimension $6$ and real dimension $12$, with real forms $O(1,3)$ on the quaternion subspace and the compact $O(4)$ on the Hermitian subspace. The natural conjugation is a $\mathbb{C}$-linear isometry carrying the form to the quaternion bilinear form. The restriction of the form to the six distinguished real subspaces and the comparison with the three sibling forms are *The Six Subspaces under the Complex Bilinear Form* and *The Four Pairings of the Biquaternion Algebra*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle\tilde P,\tilde Q\rangle=\mathrm{Sc}(\tilde P\tilde Q)=\sum_\mu\varepsilon_\mu P_\mu Q_\mu$ | the complex bilinear form |
| $\varepsilon=(1,-1,-1,-1)$ | the sign vector |
| $D=\operatorname{diag}(1,-1,-1,-1)$ | its Gram matrix in the coefficient basis; determinant $-1$; inertia $(1,3)$ |
| $\operatorname{diag}(D,-D)$ | its realified Gram matrix; signature $(4,4)$ |
| $\sum_\mu\varepsilon_\mu Q_\mu^2=0$ | the null quadric; real dimension $6$; the isotropic planes of real dimension $4$ |
| $\sum_\mu\varepsilon_\mu Q_\mu^2=1$ | the level set; a non-compact complex quadric of real dimension $6$ |
| $O_4(\mathbb{C})$ | the isometry group; real dimension $12$ |
| $O(1,3)$, $O(4)$ | its real forms on the quaternion and the Hermitian subspace |
| $\langle\tilde P^{\natural},\tilde Q\rangle=\langle\tilde P,\tilde Q\rangle_{\natural}$ | the natural conjugation carries the form to the sibling bilinear form |

## Further Reading

- *The Six Subspaces under the Complex Bilinear Form* (`articles_maths/the-six-subspaces-under-the-complex-bilinear-form.md`), for the restriction matrices, the definite rows and the isometry groups of the restrictions
- *Association and the Transpose on the Biquaternion Algebra* (`articles_maths/association-and-the-transpose-on-the-biquaternion-algebra.md`), for the transpose the form defines on the operators
- *The Four Pairings of the Biquaternion Algebra* (`articles_maths/the-four-pairings-of-the-biquaternion-algebra.md`), for the four forms, their Gram matrices, their signatures and their isometry groups
- *The Quaternion Bilinear Form on the Biquaternion Algebra* (`articles_maths/the-quaternion-bilinear-form-on-the-biquaternion-algebra.md`), for the quaternion bilinear companion of Gram matrix $\mathrm{I}_4$
- *The Four Biquaternion Complex Products* (`articles_maths/the-four-biquaternion-complex-products.md`), for the plain product whose scalar part is the form
- *Introduction to the Six Subspaces* (`articles_maths/introduction-to-the-six-subspaces.md`), for the six distinguished real subspaces
- *Bilinear Forms* (`articles_maths/bilinear-forms.md`) and *Quadratic Forms and Polarisation* (`articles_maths/quadratic-forms-and-polarisation.md`), for the general theory of bilinear forms, their Gram matrices, non-degeneracy and Sylvester's law
- *The Isotropic Structure of the Quaternion Bilinear Form* (`articles_maths/the-isotropic-structure-of-the-quaternion-bilinear-form.md`), for the companion cone the quadric must not be identified with
- Werner Greub, *Linear Algebra*, 4th edition (Springer, 1981), for the complex orthogonal groups and their real forms.
