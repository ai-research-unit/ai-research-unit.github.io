# __Biquaternion Rotations and Lorentz Transformations__

## Introduction

The biquaternion norm fixes what a motion is: the isometries of the form are the transformations that preserve $N$, and they are the rotations, the Lorentz transformations and the reflections. This article reads the reflection formula the norm supplies; the rotors of the definite form and the two-sided action are in *The Biquaternion Unit Group as a Topological Group*, and the rotation and boost directions of the trace-free subalgebra are in *Biquaternion Lie Algebra*.

The article is the Geometry slot of the Lie-theoretic block: the algebra is *Biquaternion Lie Algebra*, the group and its exponential are *Biquaternion Lie Group and Exponential Structure*, and the topology of the group is *The Biquaternion Unit Group as a Topological Group*. The reflections and the Cartan–Dieudonné theorem are stated generally in *Versors, Rotors and the Sandwich Action* and *The Clifford, Pin and Spin Groups* of Part II, and their biquaternion case is worked here; the Clifford reading of the algebra is *The Clifford Structure of the Biquaternion Algebra*; the transformation group in full is in *Biquaternion Automorphisms and Derivations*.

**Conventions.** The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_0=1,e_1,e_2,e_3$ and central scalar imaginary $i$; a general element is $\tilde{Q}=\sum_{\mu=0}^{3} Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$. The biquaternion norm is $N(\tilde{Q})=\tilde{Q}\bar{\tilde{Q}}=\sum_\mu Q_\mu^2$, and $\tilde{Q}$ is a unit exactly when $N(\tilde{Q})\neq0$ (*Biquaternion Norm and Invertibility*). Throughout, a biquaternion is written $\tilde{Q}=Q_0e_0+\mathbf{Q}$ with $\mathbf{Q}=\sum_{k=1}^3 Q_k e_k$.

---

## Reflections

The sandwich also realises the **reflections**, on the subspaces where the multiplication is Clifford. Let $v\in\mathbb{B}$ with $N(v)=1$; the reflection in the hyperplane $v^{\perp}$ is the linear map
$$
\rho_v(x)=-v\,x\,v^{-1}=-v\,x\,\bar{v},
$$
the second equality using $v^{-1}=\bar{v}/N(v)=\bar{v}$ for a norm-one element.

**Theorem.** For $v$ with $N(v)=1$ the map $\rho_v$ preserves the biquaternion norm and its polar form, satisfies $\rho_v(v)=-v$, and fixes pointwise every element that anticommutes with $v$; its square is the conjugation $\rho_v^2(x)=v^2xv^{-2}$.

**Proof.** Since $v$ is invertible, $\rho_v$ is a linear automorphism, and $N(\rho_v(x))=N(v)N(x)N(v)^{-1}=N(x)$ by multiplicativity of the norm, whence the polar form is preserved too; the statement $\rho_v(v)=-vvv^{-1}=-v$ is immediate. If $x$ anticommutes with $v$, then $-vxv^{-1}=xv\,v^{-1}=x$, so $x$ is fixed. The square is $\rho_v(\rho_v(x))=v(vxv^{-1})v^{-1}=v^2xv^{-2}$, a conjugation by $v^2$, and it is the identity exactly when $v^2$ is a scalar. $\square$

**Remark (which subspaces carry the reflections).** For the formula to be a genuine reflection, orthogonality and anticommutation must coincide on the ambient subspace. This happens when the multiplication is Clifford there: on the vector subspace $\mathrm{Vect}(\mathbb{B})=\mathbb{C}\{e_1,e_2,e_3\}$ and its real form $\mathbb{R}\{e_1,e_2,e_3\}$ one has
$$
vx+xv=-2B(v,x)\,e_0,
$$
so the hyperplane $v^{\perp}$ is exactly the set of elements anticommuting with $v$, and $\rho_v$ fixes $v^{\perp}$ pointwise, negates $v$, and has complex-linear determinant $-1$. Here $v^2=-\bigl(\sum_k v_k^2\bigr)e_0$ is a scalar, so $\rho_v$ is an involution. On the quaternion and Hermitian subspaces the elements do not anticommute, and a norm-one element acts there by conjugation as a rotation rather than as a reflection. On the algebra as a whole, likewise, $\rho_v$ has determinant $+1$ for every $v$ with $N(v)=1$, so the maps attached to the finite groups of units are rotations and not reflections; and on $\mathbb{H}_{\mathbb{B}}$ the norm-one element $e_0$ is central, so $\rho_{e_0}=-\mathrm{id}$ and nothing is fixed.

**Theorem (Cartan–Dieudonné in the biquaternion algebra).** On the complex three-dimensional vector subspace $\mathrm{Vect}(\mathbb{B})$ and on its real form $\mathbb{R}\{e_1,e_2,e_3\}$, every isometry is a product of at most three reflections $\rho_v$ with $N(v)=1$.

**Proof.** On these subspaces $N(v)=v_1^2+v_2^2+v_3^2$ is a non-degenerate form, and by the theorem above the maps $\rho_v$ with $N(v)=1$ are its reflections in the hyperplanes $v^{\perp}$; the Cartan–Dieudonné theorem, stated for a general vector space in *The Clifford, Pin and Spin Groups*, then gives generation by at most $\dim W=3$ reflections. $\square$

**Remark.** The reflections of this section are attached to the odd part $\mathrm{Vect}(\mathbb{B})$; the Lorentz reflections are not of the shape $\rho_v$ and live in the Clifford layer, not in $\mathbb{B}$.

## Summary

The motions of the biquaternion algebra are the isometries of its biquaternion norm, and they are the rotations and the Lorentz transformations. The compact summand of the trace-free subalgebra generates the rotations of the definite form and the hyperbolic summand the boosts of the indefinite one; the unit quaternions $S^3=Sp(1)$ carry the rotations by the sandwich and the norm-one group $\mathbb{B}^\times_1$ the complexified motions, with the double covers $\mathbb{B}^\times_1/\{\pm e_0\}\cong SO^+(1,3)$ and $\mathbb{B}^\times_1\cong Spin(1,3)$ realised inside the algebra — all of this in *Biquaternion Lie Algebra*, *Biquaternion Lie Group and Exponential Structure* and *The Biquaternion Unit Group as a Topological Group*.

The reflections are the maps $\rho_v(x)=-vxv^{-1}=-vx\bar v$ with $N(v)=1$, defined on the Clifford vector subspace $\mathrm{Vect}(\mathbb{B})$ and its real form, where orthogonality and anticommutation coincide; on that subspace every isometry is a product of at most three of them, by Cartan–Dieudonné. The construction is that of *Versors, Rotors and the Sandwich Action* and *The Clifford, Pin and Spin Groups* of Part II, and the full symmetry group of the algebra, wider than its isometries, is in *Biquaternion Automorphisms and Derivations*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $N(\tilde{Q})$ | Biquaternion norm; the invariant of the motions |
| $\rho_v(x)=-vxv^{-1}=-vx\bar v$ | Reflection in $v^{\perp}$ on $\mathrm{Vect}(\mathbb{B})$, $N(v)=1$ |
| $vx+xv=-2B(v,x)e_0$ | Anticommutation as orthogonality on $\mathrm{Vect}(\mathbb{B})$; then $v^{\perp}=\{x:xv=-vx\}$ |
| Cartan–Dieudonné | Every isometry of $\mathrm{Vect}(\mathbb{B})$ is at most three reflections $\rho_v$ |

## Further Reading

- John Stillwell, *Naive Lie Theory* (Springer, 2008).
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001).
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997).
- S. J. Sangwine, T. A. Ell, and N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* **21** (2011) 607–636.
