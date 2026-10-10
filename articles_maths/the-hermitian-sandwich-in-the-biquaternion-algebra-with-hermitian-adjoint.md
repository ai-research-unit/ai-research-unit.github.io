
# __The Hermitian Sandwich in the Biquaternion Algebra with Hermitian Adjoint__

## Introduction

The biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ is the one algebra in which every object of the Hermitian theory can be written down in coordinates and checked by hand. It is eight-dimensional over $\mathbb{R}$ and four-dimensional over $\mathbb{C}$, it is isomorphic to the algebra $M_2(\mathbb{C})$ of two-by-two complex matrices, its four conjugations form the Klein four-group of *The Group of Involutions*, and the Hermitian sandwich on it is the map that produces the Lorentz transformation of *Biquaternion Rotations and Lorentz Transformations*. This article is the example article of the Hermitian-adjoint group: it takes the general results — the operator $\Theta_x$, the identities on the Clifford group, the forms, positivity, the unitary slice, complete positivity — and instantiates them in $\mathbb{B}$, so that the reader has one algebra in which all of them are visible at once.

The plan is to recall the dagger of the biquaternion algebra, to identify the general sandwich with the dagger sandwich already used in the corpus, to read off the general identities of *The Hermitian Sandwich on a Hermitian Algebra with Hermitian Adjoint* in the coordinates of the involution lattice, to compute the two sectors and the unitary slice, to see that the dagger of this algebra is a positive involution in the sense of *Positivity and the Hermitian Cone of a Hermitian Algebra with Hermitian Adjoint*, and to identify the slice as $U(2)$ with determinant-one part $\mathrm{Spin}(3)$. The article carries an example and points to the corpus for the applications.

The algebra is *Biquaternions as a Vector Space over $\mathbb{C}$* and *The Clifford Algebra Representation*; the four conjugations are *The Group of Involutions*; the matrix model is *The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*; the Hermitian and anti-Hermitian subspaces are *Introduction to the Remarkable Subspaces*; the dagger sandwich and its Lorentzian application are *Biquaternion Rotations and Lorentz Transformations*; the general operator is *The Hermitian Sandwich on a Hermitian Algebra with Hermitian Adjoint*; and the general forms, positivity and slice are *Hermitian Forms on a Hermitian Algebra with Hermitian Adjoint*, *The Blade Form and the Hermitian Structure with Hermitian Adjoint*, *Positivity and the Hermitian Cone of a Hermitian Algebra with Hermitian Adjoint* and *The Unitary Slice and the Compact Real Form with Hermitian Adjoint*.

## The Dagger of the Biquaternion Algebra

**Notation.** Write $\tilde{Q} = Q_0e_0 + Q_1e_1 + Q_2e_2 + Q_3e_3$ with $Q_\mu \in \mathbb{C}$ and $e_1, e_2, e_3$ the quaternion units, so that $e_0 = 1$ and $e_k^{2} = -1$. The four conjugations are the quaternion conjugation $\bar\cdot$, the coefficient conjugation $\bar{\cdot}$, their composite **Hermitian conjugation** ${}^{*} = \bar\cdot\circ\bar{\cdot}$,

$$
\tilde{Q}^{*} = \bar{Q_0}e_0 - \bar{Q_1}e_1 - \bar{Q_2}e_2 - \bar{Q_3}e_3 ,
$$

and the reversal $\flat = -{}^{*}$. The involution ${}^{*}$ is the dagger of the corpus in this algebra.

**Proposition (the dagger is positive here).** The scalar form of the dagger is positive definite,

$$
\mathrm{Sc}\bigl(\tilde{Q}^{*}\tilde{Q}\bigr) = |Q_0|^{2} + |Q_1|^{2} + |Q_2|^{2} + |Q_3|^{2} > 0 \quad (\tilde{Q} \neq 0),
$$

so ${}^{*}$ is a positive involution of $\mathbb{B}$ and $\mathbb{B}$ is in the good case of *Positivity and the Hermitian Cone of a Hermitian Algebra with Hermitian Adjoint*.

**Proof.** Multiplying out and using $e_k^{2} = -1$, the terms $-\bar{Q_k}e_k\cdot Q_ke_k = |Q_k|^{2}$ and the cross terms $e_je_k$ for $j \neq k$ have zero scalar part, so the scalar part is the displayed sum of squares, positive for every nonzero $\tilde{Q}$.

**Remark (the two signatures).** The norm $N$ of the algebra and the scalar form of the dagger are different forms and there is no contradiction between them: $N$ is the quaternion norm, multiplicative and central, of signature $(1,3)$ on the Hermitian subspace $\mathbb{M}_+$ of *Introduction to the Remarkable Subspaces*; the scalar form of the dagger is the Euclidean form of the eight-dimensional real algebra. The Lorentzian signature lives on a subspace, the positivity lives on the whole algebra.

## The Operator

**Proposition (the sandwich is the dagger sandwich of the corpus).** The operator of *The Hermitian Sandwich on a Hermitian Algebra with Hermitian Adjoint* specialized to $\mathbb{B}$ is the map

$$
\Theta_{\tilde{Q}}(x) = \tilde{Q}\,x\,\tilde{Q}^{*} = \mathrm{H}_{\tilde{Q}}(x)
$$

of *Biquaternion Rotations and Lorentz Transformations*, §*The Dagger Sandwich*. Its two general laws read in this algebra as the composition

$$
\mathrm{H}_{\tilde{Q}\tilde{R}} = \mathrm{H}_{\tilde{Q}}\circ\mathrm{H}_{\tilde{R}},
$$

which is $\Theta_{xz} = \Theta_x\circ\Theta_z$, and the central rule

$$
\mathrm{H}_{z\tilde{Q}} = |z|^{2}\,\mathrm{H}_{\tilde{Q}} \quad (z \in \mathbb{C} \text{ central}),
$$

which is $\Theta_{ax} = a\,\sigma(a)\Theta_x$ with $\sigma$ the coefficient conjugation of $\mathbb{C}$ and $a = z$, $z\,\bar{z} = |z|^{2}$. Both are the general laws and neither is special to $\mathbb{B}$.

**Remark (why the central rule is the semilinearity).** The central rule is the biquaternion shadow of the fact that $\Theta_x$ is $A$-linear in its argument and only $\sigma$-semilinear in its parameter. In $\mathbb{B}$ the scalar field is $\mathbb{C}$ and the involution on it is the complex conjugation, so the rule $|z|^{2}$ is exactly the form $a\sigma(a)$ of the general statement; this is the example that makes the correction of *The Hermitian Sandwich on a Hermitian Algebra with Hermitian Adjoint* visible, since with the exponent $+1$ in place of ${}^{*}$ the rule would have been $z^{2}$ and the operator would not have been invariant under a phase.

## The Two Sectors and the Sectors of the Sandwich

**Theorem (the sandwich preserves the sectors).** For every unit $\tilde{Q}$, the sandwich maps the Hermitian subspace to itself and the anti-Hermitian subspace to itself:

$$
x^{\dagger} = x \ \Longrightarrow \ \mathrm{H}_{\tilde{Q}}(x)^{\dagger} = \mathrm{H}_{\tilde{Q}}(x), \qquad
x^{\dagger} = -x \ \Longrightarrow \ \mathrm{H}_{\tilde{Q}}(x)^{\dagger} = -\mathrm{H}_{\tilde{Q}}(x).
$$

**Proof.** $(\tilde{Q}x\tilde{Q}^{*})^{\dagger} = \tilde{Q}^{\dagger{}^{*}}x^{\dagger}\tilde{Q}^{*} = \tilde{Q}x\tilde{Q}^{*}$ when $x^{\dagger} = x$, and the same computation with a sign in the anti-Hermitian case; this is the general sector-preservation of *The Hermitian Sandwich on a Hermitian Algebra with Hermitian Adjoint* instantiated at ${}^{*}$.

**Corollary (the Lorentzian reading).** On the Hermitian subspace $\mathbb{M}_+\cong\mathbb{R}^{1,3}$ the sandwich acts by the Lorentz similarity, and on the unit-norm slice $|N(\tilde{Q})| = 1$ it acts by the proper orthochronous Lorentz group; the norm scaling

$$
N\bigl(\mathrm{H}_{\tilde{Q}}(x)\bigr) = |N(\tilde{Q})|^{2}\,N(x)
$$

is the general similarity statement of *The Hermitian Sandwich on a Hermitian Algebra with Hermitian Adjoint* in its biquaternion form. The transformation is worked out in *Biquaternion Rotations and Lorentz Transformations* and is not repeated here.

**Corollary (the operator is not an automorphism off the slice).** $\mathrm{H}_{\tilde{Q}}(xy) = \mathrm{H}_{\tilde{Q}}(x)\mathrm{H}_{\tilde{Q}}(y)$ holds exactly when $\tilde{Q}^{*}\tilde{Q} = 1$, which is the general unitality and automorphism theorem of *Completely Positive Maps of a Hermitian Algebra with Hermitian Adjoint*; the insertion between $x$ and $y$ is the defect $\tilde{Q}^{*}\tilde{Q}$, and the dagger sandwich is an automorphism only on the slice.

## The Unitary Slice of the Biquaternion Algebra

**Theorem.** The unitary slice of $\mathbb{B}$ is the unitary group $U(2)$ under the identification $\mathbb{B}\cong M_2(\mathbb{C})$ of *The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*, and its determinant-one part is $\mathrm{SU}(2)\cong\mathrm{Spin}(3)$.

**Proof.** The matrix model sends ${}^{*}$ to the conjugate transpose of a matrix, since its fixed space is the space of Hermitian matrices $\mathbb{M}_+$; the condition $x^{\dagger}x = 1$ is therefore the condition that the matrix be unitary, so the slice is $U(2)$, and the determinant-one part is $SU(2)$, which is $\mathrm{Spin}(3)$.

**Corollary (the slice is compact, and contains the spin group).** The general compactness theorem of *The Unitary Slice and the Compact Real Form with Hermitian Adjoint* gives the compactness of $U(2)$ without any matrix model, because the dagger of $\mathbb{B}$ is positive; and the determinant-one part is the spin group, so the biquaternion algebra exhibits in one example the compact slice, its Lie algebra of skew-Hermitian elements, the Cartan decomposition of the group of units, and the identification of the compact real form with a classical group.

**Remark (the slice differs from the norm-one slice).** The slice $U$ is $U(2)$, of real dimension four; the norm-one slice $\{|\tilde N|=1\}$ used for the Lorentz action is $SL(2,\mathbb{C})$ up to phase, of real dimension six, as in *Biquaternion Versors and the Orthogonal Group*. So the unitary slice and the Lorentz act on different carriers: $U(2)$ acts by automorphisms of the algebra and fixes the form of the dagger, while $SL(2,\mathbb{C})$ acts by the similarities of the quaternion norm, which is the Lorentz action on $\mathbb{M}_+$. The distinction is the biquaternion form of the general statement that the unitary slice adds operators and not isometries of the quadratic space.

## The Forms and Positivity in Coordinates

**Proposition (the three forms in the biquaternion algebra).** On $\tilde{Q} = \sum_\mu Q_\mu e_\mu$, $\tilde{R} = \sum_\mu R_\mu e_\mu$,

$$
h_{\dagger}(\tilde{Q},\tilde{R}) = \sum_\mu Q_{\bar{\mu}}R_\mu + (\text{blade cross terms}), \qquad
\mathrm{Sc}\bigl(\tilde{Q}^{*}\tilde{R}\bigr) = \sum_\mu Q_{\bar{\mu}}R_\mu ,
$$

so the scalar form of the dagger is the standard Hermitian form of $\mathbb{C}^{4}$ and the blade form is the coefficient form twisted by the signature of the quaternion units, as in *The Blade Form and the Hermitian Structure with Hermitian Adjoint*.

**Corollary (the cone in coordinates).** The Hermitian cone of $\mathbb{B}$ is the image of $x \mapsto x^{\dagger}x$; over the positive involution it is the cone of the $C^{*}$-algebra $M_2(\mathbb{C})$, whose scalar part is $\sum_\mu|Q_\mu|^{2}$ and whose boundary elements are the singular matrices; its restriction to the Hermitian subspace has the Lorentzian cone of $\mathbb{M}_+$ on its diagonal, which is the null cone of *The Topology of the Zero-Divisor Cone*.

## Summary

The biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes\mathbb{H}$, with Hermitian conjugation ${}^{*}$, has a **positive** dagger, since $\mathrm{Sc}(\tilde{Q}^{*}\tilde{Q}) = \sum_\mu|Q_\mu|^{2}$; the scalar form of the dagger is the Euclidean form of the algebra while the Lorentzian signature of the quaternion norm lives on the Hermitian subspace only. The general operator of the Hermitian sandwich is the dagger sandwich $\mathrm{H}_{\tilde{Q}}(x) = \tilde{Q}x\tilde{Q}^{*}$ of the corpus, with the composition law $\mathrm{H}_{\tilde{Q}\tilde{R}} = \mathrm{H}_{\tilde{Q}}\circ\mathrm{H}_{\tilde{R}}$ and the central rule $\mathrm{H}_{z\tilde{Q}} = |z|^{2}\mathrm{H}_{\tilde{Q}}$, which is the general parameter-semilinearity in coordinates; the Hermitian and anti-Hermitian sectors are preserved, the norm is scaled by $|N(\tilde{Q})|^{2}$, and the map is an automorphism exactly on the slice, all of which are the general theorems of the group in one algebra. The **unitary slice is $U(2)$**, with determinant-one part $\mathrm{SU}(2)\cong\mathrm{Spin}(3)$, compact by the general theorem and distinct from the norm-one slice $SL(2,\mathbb{C})$ that gives the Lorentz action; the forms specialize to the standard Hermitian form of $\mathbb{C}^{4}$ and to the coefficient form twisted by the signature, and the Hermitian cone is the cone of $M_2(\mathbb{C})$ with the Lorentzian cone of $\mathbb{M}_+$ on its diagonal.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_0, e_1, e_2, e_3$ | Unit and quaternion units, $e_k^{2}=-1$ |
| $\bar\cdot$, $\bar{\cdot}$, ${}^{*} = \bar\cdot\circ\bar{\cdot}$, $\flat = -{}^{*}$ | The four conjugations |
| $\mathrm{H}_{\tilde{Q}}(x) = \tilde{Q}x\tilde{Q}^{*}$ | Dagger sandwich, $=\Theta_{\tilde{Q}}$ |
| $\mathbb{M}_+$, $\mathbb{M}_-$ | Hermitian and anti-Hermitian subspaces |
| $N$ | Quaternion norm, signature $(1,3)$ on $\mathbb{M}_+$ |
| $U \cong U(2)$ | Unitary slice, $\mathrm{SU}(2)$ its determinant-one part |
| $\mathrm{Sc}(\tilde{Q}^{*}\tilde{Q}) = \sum_\mu|Q_\mu|^{2}$ | Scalar form of the dagger, positive definite |

## Further Reading

- The corpus articles *Biquaternions as a Vector Space over $\mathbb{C}$*, *The Group of Involutions*, *Introduction to the Remarkable Subspaces*, *Biquaternion Versors and the Orthogonal Group*, *Biquaternion Rotations and Lorentz Transformations* and *Topology in the Space of Biquaternions*, for the coordinate and geometric background used here.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups*, Cambridge Studies in Advanced Mathematics 50 (Cambridge University Press, 1995), for the identification of the complexified quaternions with $M_2(\mathbb{C})$ and the Lorentz group.
- Pertti Lounesto, *Clifford Algebras and Spinors*, London Mathematical Society Lecture Note Series 286 (Cambridge University Press, 2nd ed. 2001), for the complexified quaternion algebra and its involutions.
- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time*, Vol. 1 (Cambridge University Press, 1984), for the Hermitian-matrix model of Minkowski space and the $SL(2,\mathbb{C})$ action.
