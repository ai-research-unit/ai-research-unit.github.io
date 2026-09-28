# __Biquaternion Lie Group and Exponential Structure__

## Introduction

The group of units $\mathbb{B}^\times$ is a real Lie group, and its exponential map is the bridge between the group and the Lie algebra *Biquaternion Lie Algebra*. This article reads the Lie-group structure: the exponential and its parametrisation of the group, the cases of the exponential, the group law, the failure of surjectivity that the Lorentz group exhibits, and the real forms and subgroups the group carries.

The exponential itself — its series, its closed form, the logarithm and the power functions — is computed in *Biquaternion Elementary Functions*, and only its group-theoretic consequences are used here; the Lie algebra is in *Biquaternion Lie Algebra*, and the topology of the group is in *The Biquaternion Unit Group as a Topological Group*. The motions the group generates are in *Biquaternion Rotations and Lorentz Transformations*.

Physically this is the group theory of the Lorentz transformations themselves. The exponential of a pure vector is a rotation when $\nu^2=-1$, a boost when $\nu^2=+1$ and a parabolic twist when $\nu^2=0$, so the closed form is the polar decomposition of a Lorentz transformation; the domain of the exponential is where the rapidity stays finite, and its failure of surjectivity on the Lorentz group is the physical statement that not every proper orthochronous motion is a finite rotation about, or boost along, a single axis.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_0=1,e_1,e_2,e_3$ and central scalar imaginary $i$; a general element is $\tilde{Q}=\sum_{\mu=0}^{3} Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$. The biquaternion norm is $N(\tilde{Q})=\tilde{Q}\bar{\tilde{Q}}=\sum_\mu Q_\mu^2$, and $\tilde{Q}$ is a unit exactly when $N(\tilde{Q})\neq0$ (*Biquaternion Norm and Invertibility*). Throughout, a biquaternion is written $\tilde{Q}=Q_0e_0+\mathbf{Q}$ with $\mathbf{Q}=\sum_{k=1}^3 Q_k e_k$. The material and informational sectors $\mathbb{M}_-$ and $\mathbb{M}_+$ are those of *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector* and *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*.

---

## The Unit Quaternions and Their Complexification

The **unit quaternions** are the elements of $\mathbb{H}_{\mathbb{B}}$ of norm $1$:

$$
S^3 = \{q \in \mathbb{H}_{\mathbb{B}} : N(q) = 1\},
$$

a compact, connected, simply connected real Lie group of real dimension $3$. Every such $q$ is $\cos\theta\, e_0 + \sin\theta\, \hat{n}$ with $\hat{n}$ a real unit vector part, the quaternion exponential.

Complexifying the coefficients turns $N(q) = 1$ into the same equation over $\mathbb{C}$, giving the **unit-norm subgroup**

$$
\mathbb{B}^\times_1 = \{\tilde{Q} \in \mathbb{B} : N(\tilde{Q}) = 1\},
$$

whose elements need not be real quaternions.

**Dimension.** The level set $N = 1$ has complex dimension $3$ and real dimension $6$, the biquaternion norm being a submersion wherever $N(\tilde{Q}) \neq 0$. The group $\mathbb{B}^\times_1$ is connected, simply connected and non-compact, and it is the **complexification of the unit quaternions**: the trace-free subalgebra satisfies $\mathrm{B}_0 = \mathrm{K} \otimes_{\mathbb{R}} \mathbb{C}$ for the compact rotation subalgebra $\mathrm{K}$ below, and $\mathbb{B}^\times_1$ complexifies the compact group $S^3$. Its centre is

$$
Z(\mathbb{B}^\times_1) = \{\pm e_0\} \cong \mathbb{Z}/2.
$$

## The Subgroups and the Real Forms

The relevant subgroups are: $\mathbb{B}^\times$, the nonzero-norm elements (complex dimension $4$, real dimension $8$); $\mathbb{B}^\times_1$, the unit-norm elements (complex dimension $3$, real dimension $6$); the rotation group $S^3$, the unit-norm real quaternions (real dimension $3$); and the centre $\mathbb{C}^\times e_0$ of nonzero scalars (complex dimension $1$, real dimension $2$).

$S^3$ is the maximal compact subgroup of $\mathbb{B}^\times_1$, with Lie algebra the compact rotation subalgebra $\mathrm{K}$ of the section on the trace-free subalgebra. The centre $\{\pm e_0\}$ is discrete, and

$$
\mathbb{B}^\times_1/\{\pm e_0\} \cong SO^+(1,3),
$$

the proper orthochronous Lorentz group, of real dimension $6$. Hence $\mathbb{B}^\times_1$ is a two-sheeted cover of $SO^+(1,3)$ and, being simply connected, is its universal cover: it is the spin group of Lorentzian signature,

$$
\mathbb{B}^\times_1 \cong \mathrm{Spin}(1,3), \qquad \mathrm{B}_0 \cong \mathfrak{so}(1,3).
$$

The Lorentz action is rotor conjugation, $\tilde{Q} \mapsto \tilde{\Lambda}\tilde{Q}\tilde{\Lambda}^\dagger$ for $\tilde{\Lambda} \in \mathbb{B}^\times_1$, which preserves $\mathbb{M}_-$ and $N(\tilde{Q})$; its compact part is the rotation family and its non-compact part the hyperbolic rotations, with closed forms in the section on the exponential of a rotation and of a hyperbolic rotation of *Biquaternion Elementary Functions*.

**Physical reading: the double cover.** The quotient by $\{\pm e_0\}$ is the statement that the two elements $\pm\tilde{\Lambda}$ define the same Lorentz transformation, and the simple connectivity of the norm-one group is the statement that it is the *universal* cover: a Lorentz transformation is implemented by a biquaternion only up to sign, and a closed path in the Lorentz group that winds once lifts to a path joining $\tilde{\Lambda}$ to $-\tilde{\Lambda}$. This is the spinorial double cover, the algebraic origin of spin, and it is the reason the framework's spinors are elements of the minimal left ideals rather than vectors — the module-theoretic face of it is *Modules over the Biquaternion Algebra*, the geometric face *Biquaternion Spin Geometry*.

## The Unitary Subgroup and the Defining Module

The algebra acts on the defining module $\mathbb{C}^2$ by the defining representation, in which a biquaternion acts as its $2\times2$ matrix $\Phi(\tilde{Q})$ (*The 2×2 Matrix Representation of Biquaternions*). The elements that preserve the standard Hermitian form of $\mathbb{C}^2$ are exactly those with $\tilde{Q}^{\dagger}\tilde{Q}=e_0$, and they form a compact subgroup of the group of units,

$$
U(2)=\{\tilde{Q}\in\mathbb{B}^{\times}:\tilde{Q}^{\dagger}\tilde{Q}=e_0\},
$$

of real dimension $4$. The determinant-one elements inside it are the unit quaternions:

$$
U(2)\cap SL(2,\mathbb{C})=S^3=SU(2),
$$

consistently with the rotation group being the unitary part of the norm-one group. Every element of $U(2)$ is the product of a unit quaternion and a unit complex scalar, and the two factors meet in $\{\pm e_0\}$:

$$
U(2)=S^3\cdot U(1)\cong (SU(2)\times U(1))/\{\pm(1,1)\}.
$$

**Proof.** If $\tilde{Q}\in U(2)$ then $|\det\Phi(\tilde{Q})|=1$, so $P=\tilde{Q}\,(\det\Phi(\tilde{Q}))^{-1/2}\in U(2)$ has determinant one, hence lies in $S^3$ by the identification of the determinant-one unitary elements with the unit quaternions; the scalar $(\det\Phi(\tilde{Q}))^{1/2}$ is a unit complex number. The intersection $\{\pm e_0\}$ is the set of scalars $\lambda e_0$ of determinant $\lambda^2=1$, and the kernel of $S^3\times U(1)\to U(2)$, $(q,\lambda)\mapsto\lambda q$, is $\{\pm(1,1)\}$. $\square$

**Remark.** The norm-one group $\mathbb{B}^{\times}_1\cong SL(2,\mathbb{C})$ is strictly larger: it acts on the defining module too, but it does not preserve the Hermitian form, and unlike $U(2)$ it is non-compact.

**Physical reading: internal and external phases.** The splitting $U(2)=S^3\cdot U(1)$ is the statement that a compact internal transformation of a two-state system factors into the rotation of its internal direction and a global phase, meeting only in the sign. The $U(1)$ factor is the unobservable global phase; the $S^3=SU(2)$ factor is the rotation of the spin direction; and the fact that the two meet in $\{\pm e_0\}$ is the same two-to-one covering read on the compact part. The non-compact norm-one group is what the framework uses for the Lorentz action, where the Hermitian form is not preserved because boosts are not unitary; the informational sector, where the form *is* preserved, is the compact $U(2)$-world of *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*.

## Surjectivity and Its Failure for the Subgroups

The exponential of the full unit group is surjective (the section on the logarithm of *Biquaternion Elementary Functions*), but the two distinguished subgroups behave differently.

**Rotations: surjective.** Every unit quaternion is $\cos\theta\, e_0 + \sin\theta\,\hat{n} = \exp(\theta\hat{n})$, so $\exp : \mathrm{K} \to S^3$ is surjective; this is the general fact that a connected compact Lie group has a surjective exponential map.

**Lorentz group: not surjective.** The exponential $\exp : \mathrm{B}_0 \to \mathbb{B}^\times_1$ is **not** surjective: $\mathbb{B}^\times_1$ is not exponential. The element of $\mathbb{B}^\times_1$ with scalar part $-1$ and non-semi-simple behaviour, corresponding to the non-diagonalisable norm-one element with the repeated eigenvalue $-1$, is

$$
\tilde{Q} = -e_0 + \frac{i}{2}e_1 - \frac{1}{2}e_2, \qquad N(\tilde{Q}) = 1 + \left(\frac{i}{2}\right)^2 + \left(-\frac{1}{2}\right)^2 = 1.
$$

Its scalar part is $Q_0 = -1$ and its vector part has $B = 0$, so the element is non-semi-simple with the repeated eigenvalue $-1$. If $\tilde{Q} = \exp(\tilde{R})$ with $\tilde{R} \in \mathrm{B}_0$, then $R_0 = 0$, and $\tilde{R} = \mu e_0 + \tilde{N}$ with $\tilde{N}$ nilpotent and $e^\mu = -1$, hence $\mu \in i\pi(2\mathbb{Z}+1)$ and $\mathrm{Tr}(\tilde{R}) = 2\mu \neq 0$, a contradiction. The same obstruction makes $\exp$ non-surjective on the real group $SL(2,\mathbb{R})$.

**Generation versus surjectivity.** Failure of surjectivity does not mean the exponentials fail to generate: since $\mathbb{B}^\times_1$ is connected and $\exp$ is a local diffeomorphism at $0$, the image $\exp(\mathrm{B}_0)$ contains a neighbourhood of the identity and generates the group, while remaining a proper subset. Nor does simple connectivity force surjectivity: $\mathbb{B}^\times_1$ is simply connected, yet $\exp$ is not onto. The classical criteria (connected compact, connected nilpotent, or $GL(n,\mathbb{C})$) are sufficient, not necessary.

**Physical reading: finite rapidity.** The non-surjectivity is physical. A boost with rapidity $\psi$ is $\exp(\psi\hat{n})$ with $\hat{n}$ having $\hat{n}^2=+1$, and a rotation is $\exp(\theta\hat{n})$ with $\hat{n}^2=-1$; the elements not in the image are those whose decomposition requires a rotation and a boost about different axes in a way no single exponential supplies, and the explicit counterexample is the norm-one element whose only eigenvalue is $-1$ and which is nilpotent in the sense of the spectral theory. In physical language these are the transformations reached only at infinite rapidity — the parabolic, lightlike cases — precisely the elements on the edge of the null cone the polar representation cannot reach. The domain of the exponential is therefore where the rapidity stays finite, and the failure is the algebraic face of the statement that the lightlike limit is not a finite motion. The parity and reflection coset outside the identity component is governed by *Biquaternion Automorphisms and Derivations*.

---

The group of units is an open subset of $\mathbb{B}$, hence a smooth real manifold of dimension $8$, but its topology is far from that of a general open set in $\mathbb{R}^8$: it has the homotopy type of a compact group. The polar decomposition exhibits the maximal compact subgroup as a strong deformation retract, and with it determines the homotopy groups and the universal cover. Everything in this part is a statement about $\mathbb{B}^\times$ as a topological group; the topology of the ambient space and of the null cone is in *Biquaternion Topology*, and the group-theoretic detail is in *The Biquaternion Unit Group as a Topological Group*.

## The Correspondence with the Lie Algebra

The exponential is the correspondence between the group and the algebra. Its differential at the identity is the identity, so it is a local diffeomorphism onto a neighbourhood of $e_0$, and the inverse function theorem makes it a chart of $\mathbb{B}^\times$ near the identity; the tangent space at the identity is the whole algebra, since $\mathbb{B}^\times$ is open, with the commutator as bracket (*Biquaternion Lie Algebra*). The Baker–Campbell–Hausdorff series of the algebra converges near the origin and reproduces the group law there, and the group law $\exp(a)\exp(b)$ against $\exp(a+b)$ of *Biquaternion Elementary Functions* is its first two terms. The subgroups correspond to the subalgebras: the rotation subalgebra $\mathrm{K}=\mathrm{span}_{\mathbb{R}}\{e_1,e_2,e_3\}$ to $S^3$, the trace-free part $\mathrm{B}_0$ to the norm-one group $\mathbb{B}^\times_1$, and the centre $\mathbb{C}e_0$ to $\mathbb{C}^\times e_0$.

**Physical reading: the generator as an infinitesimal motion.** The correspondence is the statement that an infinitesimal Lorentz transformation — an element of $\mathfrak{so}(1,3)$ — exponentiates to a finite one, and the Baker–Campbell–Hausdorff series is the bookkeeping of how the composition of two motions differs from the motion of the sum. The commutator term is the algebraic origin of the Wigner rotation of two non-collinear boosts, the worked case of *Biquaternion Rotations and Lorentz Transformations* and *The Operator Representation of Biquaternions*.

## Summary

The group of units $\mathbb{B}^\times$ is a real Lie group of real dimension $8$, and the exponential map is its link with the Lie algebra: it is a local diffeomorphism at the identity, but it is not surjective onto the group. The unit quaternions $S^3=\{q\in\mathbb{H}_{\mathbb{B}}:N(q)=1\}$ form a compact connected simply connected subgroup of real dimension $3$, whose complexification is the norm-one group $\mathbb{B}^\times_1$ of real dimension $6$ and centre $\{\pm e_0\}$.

The subgroups are $\mathbb{B}^\times$, $\mathbb{B}^\times_1$, the rotation group $S^3$ and the centre $\mathbb{C}^\times e_0$; the maximal compact subgroup of $\mathbb{B}^\times_1$ is $S^3$, and $\mathbb{B}^\times_1/\{\pm e_0\}\cong SO^+(1,3)$, so $\mathbb{B}^\times_1\cong Spin(1,3)$ is the universal cover of the proper orthochronous Lorentz group. Over the reals these are the real forms of the group, and the correspondence with the Lie algebra attaches each subgroup to its subalgebra: $S^3$ to $\mathrm{K}$, $\mathbb{B}^\times_1$ to $\mathrm{B}_0$, and $\mathbb{C}^\times e_0$ to the centre.

Surjectivity is not uniform. The exponential is surjective onto $S^3$, a connected compact group, and not surjective onto $\mathbb{B}^\times_1$: the Lorentz group is not exponential, the obstruction a non-semi-simple element with the repeated eigenvalue $-1$, and the same obstruction occurs in $SL(2,\mathbb{R})$. Physically this is the statement that not every proper orthochronous motion is a finite rotation about, or boost along, a single axis: the exceptional elements are the infinite-rapidity, lightlike limits. The image still contains a neighbourhood of the identity and generates the connected group, so failure of surjectivity is not failure of generation.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}^\times$ | Group of units; real Lie group of real dimension $8$ |
| $\exp$ | Exponential map; closed form in *Biquaternion Elementary Functions* |
| $S^3=\{q\in\mathbb{H}_{\mathbb{B}}:N(q)=1\}$ | Unit quaternions; compact subgroup of real dimension $3$; the spatial rotations |
| $\mathbb{B}^\times_1=\{N=1\}$ | Norm-one group; complexification of $S^3$; real dimension $6$ |
| $\{\pm e_0\}$ | Centre of $\mathbb{B}^\times_1$; $\mathbb{B}^\times_1/\{\pm e_0\}\cong SO^+(1,3)$ |
| $\mathbb{B}^\times_1\cong Spin(1,3)$ | The norm-one group as the spin group of Lorentzian signature; the double cover of the Lorentz group |
| $\mathrm{B}_0\cong\mathfrak{so}(1,3)$ | Lie algebra of $\mathbb{B}^\times_1$; trace-free part |
| $\mathrm{K}=\mathrm{span}_{\mathbb{R}}\{e_1,e_2,e_3\}$ | Lie algebra of $S^3$; compact rotation subalgebra |
| $\mathbb{C}^\times e_0$ | Centre of $\mathbb{B}^\times$; Lie algebra $\mathbb{C}e_0$; the global phase |
| $\tilde{\Lambda}\tilde{Q}\tilde{\Lambda}^\dagger$ | Lorentz action by rotor conjugation |

## Further Reading

- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations: An Elementary Introduction* (Springer, 2nd ed. 2015).
- John Stillwell, *Naive Lie Theory* (Springer, 2008).
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, 1997).
