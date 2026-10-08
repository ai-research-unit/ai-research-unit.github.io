
# __The Six Subspaces under the General Plain Algebra of Biquaternions__

## Introduction

The general plain bilinear form $\langle\tilde P,\tilde Q\rangle=\mathrm{Sc}(\tilde P\tilde Q)=\sum_\mu\varepsilon_\mu P_\mu Q_\mu$ of *The Four Pairings of the Biquaternion Algebra* meets the six distinguished real subspaces of *Introduction to the Six Subspaces* — the centre $\mathbb{C}_{\mathbb{B}}$, the vector subspace $\mathrm{Vect}(\mathbb{B})$, the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, the anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$, the Hermitian subspace $\mathbb{M}_+$ and the anti-Hermitian subspace $\mathbb{M}_-$. On each of the six the realified form is a real symmetric form, and this article reads its matrix, its signature, its definite or indefinite character, its isotropic lines, its automorphism group, and the orthogonality that relates the six.

The form is used, not re-derived. Its definition, its coefficient Gram matrix $D=\operatorname{diag}(1,-1,-1,-1)$ and its comparison with the other three forms are the matter of *The Four Pairings of the Biquaternion Algebra*, and its realified signature $(4,4)$ is the matter of *The Realification of the Four Forms*; the six subspaces and their bases are the matter of *Introduction to the Six Subspaces*; and the companion reading of the same six subspaces by the general quaternionic bilinear form is *The Six Subspaces under the General Quaternionic Algebra of Biquaternions*. The other three forms on the same six subspaces are *The Six Subspaces under the General Quaternionic Algebra of Biquaternions*, *The Six Subspaces under the General Plain Sesqualgebra of Biquaternions* and *The Six Subspaces under the General Quaternionic Sesqualgebra of Biquaternions*. This article owns the restrictions themselves and the structure of each one.

## The Six Restriction Matrices

The scalar part of the product is diagonal on the units, $\mathrm{Sc}(e_\mu e_\nu)=\varepsilon_\mu\delta_{\mu\nu}$ with $\varepsilon=(1,-1,-1,-1)$, so the restriction of the form to each subspace is diagonal in its natural real basis, and the six matrices are read at once.

| Subspace | Natural real basis | Restriction matrix | Signature |
|---|---|---|---|
| Centre $\mathbb{C}_{\mathbb{B}}$ | $e_0,\,ie_0$ | $\begin{pmatrix}1&0\\0&-1\end{pmatrix}$ | $(1,1)$ |
| Vector $\mathrm{Vect}(\mathbb{B})$ | $e_1,e_2,e_3,\,ie_1,ie_2,ie_3$ | $\operatorname{diag}(-1,-1,-1,1,1,1)$ | $(3,3)$ |
| Quaternion $\mathbb{H}_{\mathbb{B}}$ | $e_0,e_1,e_2,e_3$ | $D=\operatorname{diag}(1,-1,-1,-1)$ | $(1,3)$ |
| Anti-quaternion $i\mathbb{H}_{\mathbb{B}}$ | $ie_0,ie_1,ie_2,ie_3$ | $-D=\operatorname{diag}(-1,1,1,1)$ | $(3,1)$ |
| Hermitian $\mathbb{M}_+$ | $e_0,ie_1,ie_2,ie_3$ | $\mathrm{I}_4=\operatorname{diag}(1,1,1,1)$ | $(4,0)$ |
| Anti-Hermitian $\mathbb{M}_-$ | $ie_0,e_1,e_2,e_3$ | $-\mathrm{I}_4=\operatorname{diag}(-1,-1,-1,-1)$ | $(0,4)$ |

*Proof.* Each entry is the value of the realified form, that is the real part of $\langle f_i,f_j\rangle$, on two elements of the stated basis; on the four real subspaces the form is already real-valued, and on the two complex subspaces the real part is the realified form. On the quaternion basis $(e_0,e_1,e_2,e_3)$ the values are $1,-1,-1,-1$; on the anti-quaternion basis $(ie_0,ie_1,ie_2,ie_3)$ they are $-\varepsilon_\mu$, that is $-1,1,1,1$, because $\langle ie_\mu,ie_\nu\rangle=-\varepsilon_\mu\delta_{\mu\nu}$ by the $\mathbb{C}$-bilinearity and $i^2=-1$; on the centre the two entries are $1$ and $-1$; and on the vector subspace the three entries from the real directions $e_1,e_2,e_3$ are $-1$ and the three from the imaginary directions $ie_1,ie_2,ie_3$ are $+1$, since only the sign vector distinguishes them. The two Hermitian rows are the two bases on which the form is definite, and their matrices are therefore $\pm\mathrm{I}_4$. All six bases are orthogonal for the form, so every matrix is diagonal. Verified on the six restricted Gram matrices.

**Remark (the signature is not the dimension).** No subspace is totally isotropic: the restricted form is non-degenerate on each of the six, because each displayed matrix is invertible. The two definite rows have no isotropic vector, and the four indefinite rows have isotropic vectors; their isotropic sets are computed next.

## The Definite Rows and the Maximal Definite Subspaces

Two of the six rows are definite. On the **Hermitian subspace** the form is positive definite, of signature $(4,0)$; on the **anti-Hermitian subspace** it is negative definite, of signature $(0,4)$. The two are exchanged by the central scalar,

$$
\langle i\tilde P,i\tilde Q\rangle=-\langle\tilde P,\tilde Q\rangle,
$$

which reverses the sign of the form and therefore exchanges the positive definite subspace $\mathbb{M}_+$ with the negative definite subspace $\mathbb{M}_-$.

The realified form of the whole algebra has signature $(4,4)$, so its maximal positive definite dimension and its maximal negative definite dimension are both $4$. The Hermitian subspace, of real dimension $4$ and positive definite, is therefore a **maximal positive definite subspace**, and the anti-Hermitian subspace is a **maximal negative definite subspace**; neither can be enlarged while remaining definite. The centre is a definite plane only in the hyperbolic sense — its form $(1,1)$ is neither positive nor negative definite — and the quaternion and vector subspaces contain both signs.

**Remark (the two polarisations of the realified form).** A real form of signature $(p,q)$ carries a maximal positive definite subspace of dimension $p$ and a maximal negative definite subspace of dimension $q$, and the two are orthogonal complements. Here that general statement reads: $\mathbb{M}_+$ is a maximal positive definite subspace, $\mathbb{M}_-$ is a maximal negative definite subspace, the two are orthogonal and $\mathbb{M}_+\perp\mathbb{M}_-=\mathbb{B}$, and on the splitting of an element into its Hermitian and anti-Hermitian parts the diagonal is the sum of the two restricted diagonals, the first non-negative and the second non-positive.

## The Isotropic Lines of the Indefinite Rows

The four indefinite rows are $(1,1)$ on the centre, $(3,3)$ on the vector subspace, $(1,3)$ on the quaternion subspace and $(3,1)$ on the anti-quaternion subspace. On each the isotropic set is a cone through the origin, of real dimension one less than the subspace, and one null element on each row exhibits it.

| Subspace | Signature | Null element | Null cone, real dimension |
|---|---|---|---|
| Centre | $(1,1)$ | $e_0+ie_0$ | $1$, the two lines $\mathbb{R}(e_0\pm ie_0)$ |
| Vector | $(3,3)$ | $e_1+ie_1$ | $5$ |
| Quaternion | $(1,3)$ | $e_0+e_1$ | $3$ |
| Anti-quaternion | $(3,1)$ | $ie_0+ie_1$ | $3$ |

*Proof.* Each element is null by the restricted form of its row: on the centre $q_0^2-(q'_0)^2$ gives $1-1=0$ at $e_0+ie_0$; on the vector subspace $(q'_1)^2-q_1^2$ gives $1-1=0$ at $e_1+ie_1$; on the quaternion subspace $q_0^2-q_1^2$ gives $1-1=0$ at $e_0+e_1$; and on the anti-quaternion subspace $-(q'_0)^2+(q'_1)^2$ gives $-1+1=0$ at $ie_0+ie_1$. On an indefinite form of signature $(p,q)$ the isotropic set is a cone of real dimension equal to the dimension of the space minus one, because the diagonal is a non-constant homogeneous polynomial of degree two and its zero set has codimension one; the four dimensions follow. On the centre, of dimension two, the cone is the pair of real lines $\mathbb{R}(e_0+ie_0)$ and $\mathbb{R}(e_0-ie_0)$. Verified on the four rows.

**Remark (the isotropic cones are not the null quadric).** These four cones lie inside the null quadric $\mathcal{Q}=\{\langle\tilde Q,\tilde Q\rangle=0\}$ of the whole algebra, which is of real dimension $6$ and has the apex as its only singularity. The centre meets $\mathcal{Q}$ in two real lines, the quaternion subspace in a cone of real dimension $3$, and the vector and anti-quaternion subspaces in cones of dimension $5$ and $3$. The zero-divisor cone is a different quadric and meets the six subspaces differently; the two cones agree on the Hermitian and anti-Hermitian subspaces only at the origin, since those rows are definite. On the quaternion subspace, for instance, the zero-divisor condition is $\sum_\mu Q_\mu^2=q_0^2+q_1^2+q_2^2+q_3^2=0$, which on the real quaternions holds only at the origin, while the general plain bilinear null cone is the $(1,3)$ cone computed above; on that subspace the two cones are as different as they can be.

## The Automorphism Groups of the Restrictions

**Definition.** For each subspace $V$ of the six, the **automorphism group of the restriction** is the group of real-linear maps of $V$ preserving the restriction of the form,

$$
\mathrm{Isom}\bigl(V,\langle\cdot,\cdot\rangle\bigr)=\{S\in GL_{\mathbb{R}}(V):\langle Sv,Sw\rangle=\langle v,w\rangle\text{ for all }v,w\in V\}.
$$

It is the real orthogonal group of the signature of the restriction.

| Subspace | Signature | Automorphism group | Real dimension |
|---|---|---|---|
| Centre | $(1,1)$ | $O(1,1)$ | $1$ |
| Vector | $(3,3)$ | $O(3,3)$ | $15$ |
| Quaternion | $(1,3)$ | $O(1,3)$ | $6$ |
| Anti-quaternion | $(3,1)$ | $O(3,1)\cong O(1,3)$ | $6$ |
| Hermitian | $(4,0)$ | $O(4)$ | $6$ |
| Anti-Hermitian | $(0,4)$ | $O(4)$ | $6$ |

The orthogonal group of a form of signature $(p,q)$ with $p+q=n$ has real dimension $n(n-1)/2$, the dimension of its Lie algebra of anisotropic matrices, which gives the last column: $1$ for $n=2$, $6$ for $n=4$ and $15$ for $n=6$.

**Remark (the real automorphism group against the complex one).** On the centre and the vector subspace, which are complex subspaces of the algebra, the largest $\mathbb{C}$-linear group preserving the subspace and the form is the smaller complex orthogonal group $O_1(\mathbb{C})$ on the centre and $O_3(\mathbb{C})$ on the vector subspace, of real dimensions $0$ and $6$; the real automorphism groups $O(1,1)$ and $O(3,3)$ of the table are larger because a real-linear form preservation need not respect the complex structure. On the four real subspaces $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$ and $\mathbb{M}_-$ the two groups coincide: a real automorphism of the restriction extends by complex linearity to an automorphism of the algebra preserving the subspace, and conversely. This is why the rows $O(1,3)$ and $O(4)$ of the table are the real forms of $O_4(\mathbb{C})$ of *The Four Pairings of the Biquaternion Algebra*, §*The Forms in Comparison*, while $O(1,1)$ and $O(3,3)$ are not.

**Remark (the four real-subspace rows are the real forms of the complex form).** The four real subspaces $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$ and $\mathbb{M}_-$ each span the complex algebra over $\mathbb{C}$, so each restriction is a real form of a general plain bilinear form on $\mathbb{B}$: on $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$ the complexification is a form congruent to $D$, of real form $O(1,3)$, and on $\mathbb{M}_+$ and $\mathbb{M}_-$ it is a form congruent to $\mathrm{I}_4$, of real form $O(4)$. Over $\mathbb{C}$ the matrices $D$ and $\mathrm{I}_4$ are congruent, so all four are real forms of the same complex form, and the apparent variety of the four restrictions is the variety of the real forms of one complex form and not of four different complex forms.

## The Orthogonal Splitting of the Centre and the Vector Subspace

The form is diagonal in the natural bases, so the centre and the vector subspace are mutually orthogonal and complementary:

$$
\mathbb{B}=\mathbb{C}_{\mathbb{B}}\perp\mathrm{Vect}(\mathbb{B}),\qquad
\langle\tilde Q,\tilde R\rangle=\langle\tilde Q_0,\tilde R_0\rangle+\langle\tilde Q_1,\tilde R_1\rangle,
$$

where $\tilde Q_0,\tilde R_0$ are the centre parts and $\tilde Q_1,\tilde R_1$ the vector parts. The realified form is the orthogonal sum of its restrictions, and the signatures add: $(1,1)\perp(3,3)=(4,4)$ is the signature of the whole realified form. The centre has isotropic lines and the vector subspace has an isotropic cone of dimension $5$, so the splitting is not into definite pieces; the definite pieces are the Hermitian and anti-Hermitian subspaces of the previous section.

**Remark (three orthogonal splittings).** The realified form is diagonal on three pairs of complementary subspaces, and each pair gives an orthogonal decomposition of the algebra: $\mathbb{B}=\mathbb{H}_{\mathbb{B}}\perp i\mathbb{H}_{\mathbb{B}}$, of signatures $(1,3)\perp(3,1)$; $\mathbb{B}=\mathbb{M}_+\perp\mathbb{M}_-$, of signatures $(4,0)\perp(0,4)$; and $\mathbb{B}=\mathbb{C}_{\mathbb{B}}\perp\mathrm{Vect}(\mathbb{B})$, of signatures $(1,1)\perp(3,3)$. The three decompositions add to the same $(4,4)$ and are the three readings of the one split form.

## Worked Examples

**The quaternion row in coordinates.** On the quaternion subspace with $\tilde Q=q_0e_0+q_1e_1+q_2e_2+q_3e_3$ and $\tilde R$ likewise, the restriction is $\langle\tilde Q,\tilde R\rangle=q_0r_0-q_1r_1-q_2r_2-q_3r_3$, the scalar product of signature $(1,3)$: the real scalar direction is positive and the three vector directions are negative.

**The Hermitian row in coordinates.** On the Hermitian subspace with $\tilde Q=q_0e_0+q'_1ie_1+q'_2ie_2+q'_3ie_3$ the restriction is $\langle\tilde Q,\tilde R\rangle=q_0r_0+q'_1r'_1+q'_2r'_2+q'_3r'_3$, the standard positive definite inner product of $\mathbb{R}^4$; on the anti-Hermitian subspace the same formula is negative, and the two are the two definite rows.

**The vector null cone.** On the vector subspace the restriction is $\sum_k((q'_k)^2-q_k^2)$, so the null cone is $\{\sum_k q_k^2=\sum_k(q'_k)^2\}$, of real dimension $5$; it contains the totally isotropic real plane $\mathrm{span}_{\mathbb{R}}\{e_1+ie_1,e_2+ie_2\}$, and indeed $\mathrm{span}_{\mathbb{R}}\{e_k+ie_k:k=1,2,3\}$ is totally isotropic of real dimension $3$, the maximum for signature $(3,3)$.

**The centre's two lines.** On the centre the restriction is $q_0^2-(q'_0)^2$, whose null set is the two real lines $\mathbb{R}(e_0+ie_0)$ and $\mathbb{R}(e_0-ie_0)$; the two are the isotropic lines of the hyperbolic plane $(1,1)$ and are exchanged by multiplication by $i$.

**The two definite rows have no null element.** On the Hermitian subspace the diagonal is the sum of four squares, $q_0^2+(q'_1)^2+(q'_2)^2+(q'_3)^2$, which vanishes only at the origin, and on the anti-Hermitian subspace the diagonal is its negative; the two definite rows therefore contribute no null line to the null quadric, which is why the isotropic lines above are four and not six.

**The anti-quaternion row.** On the anti-quaternion subspace the restriction is $-(q'_0)^2+(q'_1)^2+(q'_2)^2+(q'_3)^2$, the mirror of the quaternion row; the null element $ie_0+ie_1$ spans one of its null lines, and the row is the sign-mirror $(3,1)$ of the quaternion row $(1,3)$.

**An automorphism of the centre.** The hyperbolic rotation $e_0\mapsto\cosh u\,e_0+\sinh u\,ie_0$, $ie_0\mapsto\sinh u\,e_0+\cosh u\,ie_0$ preserves $q_0^2-(q'_0)^2$ for every real $u$; it generates the one-parameter group $O(1,1)$ of real dimension $1$, and it is the two-dimensional model of the hyperbolic rotation of the quaternion row.

**An automorphism of the quaternion row.** The hyperbolic rotation $e_0\mapsto\cosh u\,e_0+\sinh u\,e_1$, $e_1\mapsto\sinh u\,e_0+\cosh u\,e_1$ with $e_2,e_3$ fixed preserves the $(1,3)$ restriction of the quaternion subspace, and it is one of the generators of $O(1,3)$; together with the rotations of the vector subspace it generates the identity component of the group.

## Summary

On the six distinguished real subspaces the general plain bilinear form carries the restrictions $\begin{pmatrix}1&0\\0&-1\end{pmatrix}$ on the centre, $\operatorname{diag}(-1,-1,-1,1,1,1)$ on the vector subspace, $D$ on the quaternion subspace, $-D$ on the anti-quaternion subspace, $\mathrm{I}_4$ on the Hermitian subspace and $-\mathrm{I}_4$ on the anti-Hermitian subspace, of signatures $(1,1)$, $(3,3)$, $(1,3)$, $(3,1)$, $(4,0)$ and $(0,4)$. The Hermitian subspace is the maximal positive definite one and the anti-Hermitian the maximal negative definite one, both of dimension $4$, the two definite rows of the realified signature $(4,4)$. The four indefinite rows have isotropic cones of real dimensions $1$, $5$, $3$ and $3$, with the null elements $e_0+ie_0$, $e_1+ie_1$, $e_0+e_1$ and $ie_0+ie_1$. The automorphism groups are $O(1,1)$, $O(3,3)$, $O(1,3)$, $O(3,1)$, $O(4)$ and $O(4)$, of real dimensions $1$, $15$, $6$, $6$, $6$ and $6$. The centre and the vector subspace are orthogonal complements. The same six subspaces under the other three pairings are *The Six Subspaces under the General Quaternionic Algebra of Biquaternions*, *The Six Subspaces under the General Plain Sesqualgebra of Biquaternions* and *The Six Subspaces under the General Quaternionic Sesqualgebra of Biquaternions*, where the transposition of this table with the general quaternionic bilinear one is read on the four real forms.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle\tilde P,\tilde Q\rangle=\sum_\mu\varepsilon_\mu P_\mu Q_\mu$ | the restricted form on each subspace |
| $(1,1),(3,3),(1,3),(3,1),(4,0),(0,4)$ | the six signatures |
| $D$, $-D$, $\mathrm{I}_4$, $-\mathrm{I}_4$ | the quaternion, anti-quaternion, Hermitian and anti-Hermitian restriction matrices |
| $e_0+ie_0$, $e_1+ie_1$, $e_0+e_1$, $ie_0+ie_1$ | the null elements of the four indefinite rows |
| $O(1,1)$, $O(3,3)$, $O(1,3)$, $O(3,1)$, $O(4)$ | the automorphism groups of the six restrictions |
| $\mathbb{C}_{\mathbb{B}}\perp\mathrm{Vect}(\mathbb{B})$ | the orthogonal splitting of the algebra |
| $\mathbb{H}_{\mathbb{B}}\perp i\mathbb{H}_{\mathbb{B}}$ | the split $(1,3)\perp(3,1)$ of the algebra |
| $\mathbb{M}_+\perp\mathbb{M}_-$ | the split $(4,0)\perp(0,4)$ of the algebra |

## Further Reading

- *Introduction to the Six Subspaces* (`articles_maths/introduction-to-the-six-subspaces.md`), for the six distinguished real subspaces and their bases
- *The Six Subspaces under the General Quaternionic Algebra of Biquaternions* (`articles_maths/the-six-subspaces-under-the-general-quaternionic-algebra-of-biquaternions.md`), for the companion table of the same six subspaces
- *The Six Subspaces under the General Plain Sesqualgebra of Biquaternions* (`articles_maths/the-six-subspaces-under-the-general-plain-sesqualgebra-of-biquaternions.md`), *The Six Subspaces under the General Quaternionic Sesqualgebra of Biquaternions* (`articles_maths/the-six-subspaces-under-the-general-quaternionic-sesqualgebra-of-biquaternions.md`) and *The Six Subspaces under the Real Biquaternion Algebra* (`articles_maths/the-six-subspaces-under-the-real-biquaternion-algebra.md`), for the same six subspaces under the other readings
- *The Four Pairings of the Biquaternion Algebra* (`articles_maths/the-four-pairings-of-the-biquaternion-algebra.md`), for the form, its coefficient Gram matrix $D$, its null quadric, its value-one set and the four forms on the six subspaces, side by side
- *The Realification of the Four Forms* (`articles_maths/the-realification-of-the-four-forms.md`), for the realified signature $(4,4)$ of the form and the four realified tables side by side
