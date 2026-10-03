
# __Split-Biquaternion Exponential and Lie Group Structure__

## Introduction

The split biquaternion algebra is a real associative algebra of dimension eight, and as such it carries a Lie algebra structure under the commutator, an exponential map into its group of units, and the Lie-group structures attached to the two. This article records the Lie algebra and its decomposition into the two halves, the exponential with its closed form and its kernel, the group of units and the norm-one group, the elliptic and hyperbolic one-parameter subgroups, the polar and exponential parametrisation of an element, and the comparison with the biquaternion case. The algebra and its decomposition are used from *Split-Biquaternion Algebra* and *Split-Biquaternion Ideals and Peirce Decomposition*; the quaternion exponential is that of the companion article on the quaternions.

The treatment is purely mathematical. No physics is invoked; the "Lorentz group" is not used here, and the compact and non-compact subgroups discussed below are named for their mathematical position in the classification of one-parameter subgroups.

## The Algebra as a Lie Algebra and Its Two Halves

**Definition.** The **commutator bracket** on $\mathbb{H}_{\mathbb{D}}$ is $[\tilde Q,\tilde P] = \tilde Q\tilde P - \tilde P\tilde Q$. With this bracket $\mathbb{H}_{\mathbb{D}}$ is a real Lie algebra of dimension $8$, and it is the Lie algebra of its own group of units.

**Theorem.** In the components of the isomorphism $\mathbb{H}_{\mathbb{D}} \cong \mathbb{H} \oplus \mathbb{H}$ the bracket is componentwise,

$$
\left[(\tilde Q_+,\tilde Q_-), (\tilde P_+,\tilde P_-)\right] = \left([\tilde Q_+,\tilde P_+], [\tilde Q_-,\tilde P_-]\right) ,
$$

so that the two halves $\mathbb{H} \tilde\Pi_+$ and $\mathbb{H} \tilde\Pi_-$ are commuting ideals and $\mathbb{H}_{\mathbb{D}} \cong \mathbb{H} \oplus \mathbb{H}$ as Lie algebras.

**Proof.** The decomposition is a ring direct sum, so the commutator of pairs is the pair of commutators.

**Corollary.** The centre of the Lie algebra is $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}} \cong \mathbb{D}$, of dimension $2$; the derived algebra is $[\mathbb{H}_{\mathbb{D}}, \mathbb{H}_{\mathbb{D}}] = \mathrm{Im}\,\mathbb{H} \oplus \mathrm{Im}\,\mathbb{H} \cong \mathrm{SO}(3) \oplus \mathrm{SO}(3) \cong \mathrm{SO}(4)$, of dimension $6$; and

$$
\mathbb{H}_{\mathbb{D}} \cong \mathbb{R}^2 \oplus \mathrm{SO}(3) \oplus \mathrm{SO}(3) ,
$$

a reductive Lie algebra whose semisimple part is $\mathrm{SO}(4)$.

**Proof.** In the quaternion Lie algebra $\mathbb{H}$ the commutator of two elements is the vector product of their vector parts, so the centre is $\mathbb{R}e_0$ and the derived algebra is $\mathrm{Im}\,\mathbb{H} \cong \mathrm{SU}(2) \cong \mathrm{SO}(3)$; taking two copies, the centre is $\mathbb{R} \tilde\Pi_+ \oplus \mathbb{R} \tilde\Pi_- = \mathbb{D} e_0$ and the derived algebra is the sum of the two copies of $\mathrm{SO}(3)$. The isomorphism $\mathrm{SO}(3)\oplus\mathrm{SO}(3)\cong\mathrm{SO}(4)$ is standard.

## The Exponential

### The Series and the Closed Form

**Definition.** For $\tilde Q \in \mathbb{H}_{\mathbb{D}}$ the **exponential** is $\exp(\tilde Q) = \sum_{n\geq0} \tilde Q^n/n!$, and it converges for every $\tilde Q$ because the algebra is finite-dimensional.

**Theorem.** $\exp$ commutes with the splitting: $\exp(\tilde Q_+,\tilde Q_-) = (\exp\tilde Q_+, \exp\tilde Q_-)$. For a quaternion $q = a + \mathbf{u}$ with $a \in \mathbb{R}$ and $\mathbf{u} \in \mathrm{Im}\,\mathbb{H}$,

$$
\exp(q) = e^{a}\left(\cos|\mathbf{u}| + \frac{\mathbf{u}}{|\mathbf{u}|}\sin|\mathbf{u}|\right) , \qquad \mathbf{u} \neq 0 ,
$$

and $\exp(a) = e^{a}e_0$ for the real case $\mathbf{u} = 0$.

**Proof.** The exponential of a direct sum is the pair of exponentials. For the quaternion formula, write $q = a + \mathbf{u}$ with $a$ central and $\mathbf{u}^2 = -|\mathbf{u}|^2$, separate the series into even and odd parts, and use $\cos$ and $\sin$.

So the exponential in the split biquaternion algebra is the pair of quaternion exponentials, one per half, and the closed form follows from the formula above componentwise.

### The Group Law

**Theorem.** For $a, b \in \mathbb{H}_{\mathbb{D}}$, if $[a,b] = 0$ then $\exp(a)\exp(b) = \exp(a+b)$; conversely, if $\exp(ta)\exp(tb) = \exp(t(a+b))$ for all real $t$, then $[a,b] = 0$. In general $\exp(a)\exp(b) = \exp\left(a + b + \tfrac{1}{2}[a,b] + \cdots\right)$ by the Baker–Campbell–Hausdorff formula, so the commutator is the first obstruction.

**Proof.** The equality holds for commuting elements termwise in the series. For the converse, comparing the second derivative at $t = 0$ of the two sides of $\exp(ta)\exp(tb) = \exp(t(a+b))$ gives $a^2 + 2ab + b^2 = a^2 + ab + ba + b^2$, hence $ab = ba$.

### Surjectivity and the Kernel

**Theorem.** $\exp : \mathbb{H}_{\mathbb{D}} \to \mathbb{H}_{\mathbb{D}}^{\times}$ is surjective, and its kernel is

$$
\ker\exp = \left\{ (q_+, q_-) : \exp q_+ = \exp q_- = 1 \right\} ,
$$

where for a quaternion $q$, $\exp q = 1$ if and only if $q = 0$ or $q = 2\pi k\,\hat{\mathbf{u}}$ with $k \in \mathbb{Z}_{>0}$ and $\hat{\mathbf{u}}$ a unit imaginary quaternion.

**Proof.** Surjectivity is componentwise: every nonzero quaternion has a polar form $q = r\hat{q}$ with $r > 0$ and $\hat q$ a unit quaternion, and $\hat q = \cos\theta + \sin\theta\,\hat{\mathbf{u}}$ is $\exp(\theta\hat{\mathbf{u}})$, so $\exp(\log r + \theta\hat{\mathbf{u}}) = q$; applying this in each half gives surjectivity onto the units. For the kernel, $\exp(a + \mathbf{u}) = 1$ gives $e^a\cos|\mathbf{u}| = 1$ and $e^a\sin|\mathbf{u}|\,\hat{\mathbf{u}} = 0$; if $\mathbf{u} = 0$ then $e^a = 1$ and $a = 0$, while if $\mathbf{u} \neq 0$ then $\sin|\mathbf{u}| = 0$ forces $a = 0$ and $|\mathbf{u}| \in 2\pi\mathbb{Z}_{>0}$.

The kernel is therefore a union of a point and countably many two-spheres in each half, and the exponential fails to be injective in the same manner as the quaternion exponential.

## The Group of Units

**Theorem.** Under the splitting, the group of units is

$$
\mathbb{H}_{\mathbb{D}}^{\times} \cong \mathbb{H}^{\times} \times \mathbb{H}^{\times} \cong \mathbb{R}_{>0}^{2} \times S^{3} \times S^{3} ,
$$

a connected real Lie group of dimension $8$.

**Proof.** An element of a product ring is a unit exactly when both components are units, and $\mathbb{H}^{\times}$ is the set of nonzero quaternions, which by the polar form is $\mathbb{R}_{>0} \times S^3$.

The unit group is connected and, since $\mathbb{R}_{>0}$ is contractible and $S^3$ is simply connected, it is simply connected; its Lie algebra is $\mathbb{H}_{\mathbb{D}}$ with the commutator bracket, of dimension $8$.

## The Norm-One Group

**Definition.** The **norm-one group** of the algebra is $G_1 = \{ \tilde{S} \in \mathbb{H}_{\mathbb{D}} : N(\tilde{S}) = e_0 \}$.

**Theorem.** $G_1 = S^3 \times S^3 \cong \mathrm{Spin}(4)$, a compact connected six-dimensional Lie group.

**Proof.** Since $N(\tilde{S}) = N_+(\tilde{S})\tilde\Pi_+ + N_-(\tilde{S})\tilde\Pi_-$ and $N_\pm(\tilde{S}) = |\tilde{S}_\pm|^2$, the condition $N(\tilde{S}) = e_0$ is the pair $|\tilde{S}_+| = |\tilde{S}_-| = 1$, so $G_1$ is the product of two unit spheres, and $S^3\times S^3 \cong \mathrm{Spin}(4)$ is the standard double cover of $SO(4)$.

The norm-one group is the compact part of the unit group: every unit is a positive real scale in each component times an element of $G_1$.

## The Hyperbolic and Elliptic Subgroups

### The Elliptic Subgroups

**Theorem.** Let $\hat{\mathbf{u}}$ be a unit element of $\mathrm{Im}\,\mathbb{H}$, so $\hat{\mathbf{u}}^2 = -e_0$. Then $e^{t\hat{\mathbf{u}}} = \cos t\,e_0 + \sin t\,\hat{\mathbf{u}}$ lies in the norm-one group, and the elements $e^{t\hat{\mathbf{u}}}$ and $e^{t j\hat{\mathbf{u}}}$ generate compact one-parameter subgroups, since $(j\hat{\mathbf{u}})^2 = -e_0$ as well.

**Proof.** $\hat{\mathbf{u}}^2 = -e_0$ gives the trigonometric form directly; and $(j\hat{\mathbf{u}})^2 = j^2\hat{\mathbf{u}}^2 = (+1)(-e_0) = -e_0$, so the same form applies to $j\hat{\mathbf{u}}$. Both elements have unit norm.

The elliptic subgroups are the compact rotations: the group generated is a copy of $SO(2)$ in each case, and the two-sphere of roots of $-e_0$ in $\mathbb{M}_-$, namely the unit imaginary quaternions, parametrises them, as treated in *Split-Biquaternion Roots of Minus One*.

### The Hyperbolic Subgroups

**Theorem.** The central element $j$ satisfies $j^2 = +e_0$, and $e^{tj} = \cosh t\,e_0 + \sinh t\,j$ is a one-parameter subgroup of the units generated by $j$; any element $\tilde Q$ with $\tilde Q^2 = +e_0$ is one of $\pm e_0, \pm j$.

**Proof.** The series for $\exp(tj)$ splits into even and odd parts using $j^2 = e_0$. For the second statement, $\tilde Q^2 = e_0$ in the components $\tilde Q_\pm$ gives $\tilde Q_\pm^2 = e_0$ in the quaternion division algebra $\mathbb{H}$, whose solutions are $\tilde Q_\pm = \pm e_0$; hence $\tilde Q$ is one of $(\pm 1, \pm 1)$, that is $\pm e_0$ or $\pm j$.

The hyperbolic one-parameter subgroups are thus generated by the central element $j$, the compact ones by the imaginary quaternion directions of the two halves together with the Hermitian imaginary directions $j\hat{\mathbf{u}}$. The absence of nilpotent elements means there are no parabolic one-parameter subgroups inside the algebra, as recorded in *Split-Biquaternion Rotations and the Lorentz Group*.

## Polar and Exponential Parametrisation

**Theorem.** Every nonzero $\tilde{Q} \in \mathbb{H}_{\mathbb{D}}$ has a componentwise polar form

$$
\tilde{Q} = r_+ \hat{q}_+ \tilde\Pi_+ + r_- \hat{q}_- \tilde\Pi_- , \qquad r_\pm = |\tilde{Q}_\pm| > 0 , \ \ \hat{q}_\pm \in S^3 ,
$$

and every unit has an exponential parametrisation $\tilde{Q} = \exp(\tilde P)$ with $\tilde P = (\tilde P_+, \tilde P_-)$ and $\tilde P_\pm$ in the quaternion logarithm of $\tilde{Q}_\pm$.

**Proof.** Apply the polar form and the logarithm of a nonzero quaternion in each half.

Under this parametrisation the norm-one group is the exponential image of the traceless-with-unit-sign part, and the hyperbolic central factor is the exponential of the central line $\mathbb{R} j$. The partial failure of a single global polar form with a split complex scalar — as opposed to the componentwise form above — is exactly the zero divisor phenomenon.

## Comparison with the Biquaternion Case

In the biquaternion case the algebra $\mathbb{B} \cong M_2(\mathbb{C})$ is simple with Lie algebra $\mathrm{GL}(2,\mathbb{C})$, its group of units is $GL(2,\mathbb{C})$ of real dimension $8$, and the norm-one slice corresponds to $SL(2,\mathbb{C})$; the exponential is surjective onto $GL(2,\mathbb{C})$ and the compact retract is $U(2)$. In the split biquaternion case the algebra is the reductive Lie algebra $\mathbb{R}^2\oplus\mathrm{SO}(3)\oplus\mathrm{SO}(3) \cong \mathbb{R}^2\oplus\mathrm{SO}(4)$, the group of units is $\mathbb{R}_{>0}^2\times S^3\times S^3$, and the norm-one group is the compact $S^3\times S^3$ rather than a non-compact $SL(2,\mathbb{C})$. The exponential is again surjective onto the units, with a kernel described componentwise. The compact/non-compact split is measured by the two factors: the biquaternion unit group is a complex group of dimension $8$ whose maximal compact subgroup is $U(2)$, while the split biquaternion unit group is the product of two copies of $SU(2)$ times two positive rays, and its maximal compact subgroup is $S^3\times S^3$. The elliptic and hyperbolic one-parameter subgroups both occur, the elliptic from the imaginary directions with square $-e_0$ and the hyperbolic from the central $j$ with square $+e_0$.

## Summary

The split biquaternion algebra is a real Lie algebra of dimension $8$ under the commutator, the direct sum $\mathbb{H}\oplus\mathbb{H}$ of the two halves, with centre $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}\cong\mathbb{D}$ and derived algebra $\mathrm{SO}(3)\oplus\mathrm{SO}(3)\cong\mathrm{SO}(4)$; it is reductive, $\mathbb{R}^2\oplus\mathrm{SO}(4)$. Its exponential commutes with the splitting and has the quaternion closed form componentwise, $e^{a}(\cos|\mathbf{u}| + \hat{\mathbf{u}}\sin|\mathbf{u}|)$; the group law holds for commuting arguments and its failure is measured by the commutator; and the exponential is surjective onto the units, with kernel the pairs of quaternions of the form $2\pi k\hat{\mathbf{u}}$. The group of units is $\mathbb{H}_{\mathbb{D}}^\times \cong \mathbb{H}^\times\times\mathbb{H}^\times \cong \mathbb{R}_{>0}^2\times S^3\times S^3$, connected, simply connected, of dimension $8$, and the norm-one group is the compact $S^3\times S^3\cong\mathrm{Spin}(4)$. The elliptic one-parameter subgroups are generated by elements with square $-e_0$, which include the imaginary quaternion directions and the Hermitian imaginary directions $j\hat{\mathbf{u}}$; the hyperbolic ones are generated by the central $j$ with square $+e_0$, the only noncentral solutions of $\tilde Q^2 = e_0$ being absent. Every element has a componentwise polar form and every unit an exponential parametrisation. Compared with the biquaternion case, the simple algebra $\mathrm{GL}(2,\mathbb{C})$ is replaced by the reductive $\mathbb{R}^2\oplus\mathrm{SO}(4)$, the unit group $GL(2,\mathbb{C})$ by $\mathbb{R}_{>0}^2\times S^3\times S^3$, and the non-compact $SL(2,\mathbb{C})$ slice by the compact $\mathrm{Spin}(4)$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}_{\mathbb{D}} = \mathbb{D}\otimes_{\mathbb{R}}\mathbb{H} \cong \mathbb{H}\oplus\mathbb{H}$ | Split biquaternion algebra |
| $[\tilde Q,\tilde P] = \tilde Q\tilde P - \tilde P\tilde Q$ | Commutator, the Lie bracket |
| $\mathrm{Im}\,\mathbb{H}$ | Imaginary quaternions, $\cong \mathrm{SO}(3)$ |
| $\mathbb{H}_{\mathbb{D}} \cong \mathbb{R}^2\oplus\mathrm{SO}(4)$ | Reductive Lie algebra structure |
| $\exp(\tilde Q) = \sum \tilde Q^n/n!$ | Exponential map |
| $e^{t\hat{\mathbf{u}}} = \cos t + \sin t\,\hat{\mathbf{u}}$ | Elliptic one-parameter subgroup, $\hat{\mathbf{u}}^2 = -e_0$ |
| $e^{tj} = \cosh t + \sinh t\,j$ | Hyperbolic one-parameter subgroup, $j^2 = +e_0$ |
| $\mathbb{H}_{\mathbb{D}}^{\times} \cong \mathbb{R}_{>0}^2\times S^3\times S^3$ | Group of units, connected, dimension $8$ |
| $N(\tilde{Q}) = \tilde{Q}\tilde{Q}^{\natural}$ | Split-Biquaternion norm |
| $G_1 = \{ \tilde{S} : N(\tilde{S}) = e_0 \} = S^3\times S^3 \cong \mathrm{Spin}(4)$ | Norm-one group |
| $\ker\exp$ | Pairs of quaternions $2\pi k\hat{\mathbf{u}}$ |
| $\tilde{Q} = r_+\hat{q}_+ \tilde\Pi_+ + r_-\hat{q}_- \tilde\Pi_-$ | Componentwise polar form |

## Further Reading

- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations*, 2nd edition, Graduate Texts in Mathematics 222 (Springer, 2015), for the exponential map, the Baker–Campbell–Hausdorff formula and the structure of compact Lie groups.
- John Stillwell, *Naive Lie Theory* (Springer, 2008), for the quaternion exponential, the unit sphere $S^3$ and the double cover $\mathrm{Spin}(4)\to SO(4)$.
- Nathan Jacobson, *Lie Algebras* (Dover, 1979), for reductive Lie algebras, derived algebras and the classification of one-parameter subgroups.
- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings*, Grundlehren der mathematischen Wissenschaften 294 (Springer, 1991), for the exponential of an algebra with a nonsingular trace form.
