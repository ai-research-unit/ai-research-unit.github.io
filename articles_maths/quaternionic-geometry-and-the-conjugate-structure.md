
# __Quaternionic Geometry and the Conjugate Structure__

## Introduction

A quaternionic structure on a manifold is a rank-three bundle $\mathcal{Q}\subseteq\operatorname{End}(TM)$ of complex structures modelled on the imaginary quaternions $e_1,e_2,e_3$, and the sphere of complex structures compatible with it at a point is parametrised by the unit sphere $S^2$ inside $\mathcal{Q}$. The quaternion algebra carries a canonical involution, the **conjugation** $\lambda\mapsto\bar\lambda$, and it acts on the imaginary part by $e_i\mapsto-e_i$. The involution this induces is the **conjugate structure**: at each point it is the free involution $J\mapsto-J$ of the sphere of compatible complex structures, and on the bundle it is the corresponding bundle involution, whose fixed points form the real and the conjugate structures in the sense made precise below. This article treats the conjugate structure, its compatibility with the quaternionic Kähler condition, and the invariance of the fundamental four-form.

The conjugate structure is the *involution on the elements* of the category: the quaternionic structure is read together with the conjugation on the quaternion algebra, and the statements are those that involve the conjugation alone. The operator layer built from the conjugation — the adjoints of the quaternionic operators, the unitary quaternionic groups — belongs to the `- * Operator Theory` group of the category and is not touched here.

**The boundaries.** The quaternionic structure, the almost quaternionic level, the Obata connection, the quaternionic Kähler condition and the holonomy $Sp(n)\cdot Sp(1)$ are *Quaternionic Geometry*, the article immediately preceding this one in the same group, and nothing of it is re-derived. The hyperkähler case is *Hyperkähler Geometry*; the conjugate structure there is the subject of *Hyperkähler Manifolds and the Twistor Space*. The quaternion algebra, its conjugation and its norm are those of Part I; the Riemannian metric, the Levi-Civita connection and the holonomy group are *Riemannian Geometry*; the almost complex and Hermitian structures are *Hermitian Geometry and Almost Complex Structures*, and the Kähler condition *Kähler Geometry*. The base field is $\mathbb{R}$.

## The Conjugation

**Definition.** The **conjugation** of the quaternion algebra is the involution $\lambda\mapsto\bar\lambda$ that fixes the scalars and negates the imaginary part, so that $\overline{\lambda\mu}=\bar\mu\bar\lambda$ and $\lambda\bar\lambda=\lvert\lambda\rvert^2$. On the imaginary unit sphere it acts by $e_i\mapsto-e_i$, and it is the restriction of the central element $-1$ of the unit quaternions under the map $\lambda\mapsto\lambda\cdot\lambda^{-1}$ on the unit sphere.

**Definition.** Let $V$ be a quaternionic vector space with structure $\rho : \mathbb{H}\to\operatorname{End}(V)$, $J_i=\rho(e_i)$. The **conjugate quaternionic vector space** $\bar V$ is the real vector space $V$ with the conjugated scalar action

$$
\lambda\cdot_{\bar V}v = \bar\lambda\cdot_V v ,
$$

so that the conjugated structure is $\bar J_i=\rho(\overline{e_i})=-J_i$.

**Proposition.** The assignment $J_i\mapsto-J_i$ is a quaternionic structure with the same multiplication table, $(-J_1)(-J_2)=J_1J_2=J_3$ and $(-J_1)^2=-\mathrm{id}$; it is the transposed action of $\overline{\ }$ under $\rho$, it is an involution of the set of quaternionic structures on $V$, and it is free: no quaternionic structure on a non-zero space is fixed.

**Proof.** The relations are the relations of $J_1,J_2,J_3$ with each generator replaced by its negative, and every product in the table has two factors, so no sign changes; the identification with the conjugate module is the definition of $\bar V$; the map is involutive because the conjugation is; it is free because a fixed structure would satisfy $J_i=-J_i$, that is $2J_i=0$, forcing $J_i=0$, which $J_i^2=-\mathrm{id}$ forbids in a real vector space.

**Proposition (the sphere of complex structures).** The compatible complex structures of the quaternionic structure are $\{I_{(a,b,c)}=aJ_1+bJ_2+cJ_3 : a^2+b^2+c^2=1\}$, a two-sphere; the conjugation acts on it as the antipodal map $I\mapsto-I$, and it acts on the parametrising sphere $S^2$ as the antipode.

**Proof.** $I^2=(a^2+b^2+c^2)(-\mathrm{id})+ab(J_1J_2+J_2J_1)+\cdots=-\mathrm{id}$ by the relations, so every unit parameter gives a complex structure, and the correspondence is bijective; the conjugation negates the three coordinates.

**Remark (the two-dimensional analogue).** A complex structure is a single $J$ with $J^2=-\mathrm{id}$, and the conjugation $J\mapsto-J$ is the analogous free involution, with the conjugate complex structure of *Complex Manifolds* as the conjugate module; the quaternionic case is the generalisation in which the parameter space is a sphere rather than a pair of points.

## The Conjugate Structure on a Manifold

**Definition.** Let $(M,\mathcal{Q})$ be an almost quaternionic manifold. The **conjugate structure** is the bundle involution

$$
\sigma : \mathcal{Q}\longrightarrow\mathcal{Q}, \qquad \sigma(J)=-J ,
$$

together with the conjugate quaternionic structures on the tangent spaces; it is locally the conjugation of the quaternion algebra acting on the local trivialisation $\mathcal{Q}=\mathbb{R}^3\otimes\mathcal{O}$.

**Proposition.** The involution $\sigma$ is well defined on an almost quaternionic manifold, it is the unique bundle involution restricting at each point to the antipode of the sphere of compatible complex structures, it commutes with the structure group of $\mathcal{Q}$, and it is parallel for the Obata connection of a quaternionic manifold; the conjugate of an almost quaternionic structure is again an almost quaternionic structure.

**Proof.** A local trivialisation of $\mathcal{Q}$ is determined up to the action of $GL(n,\mathbb H)\cdot Sp(1)$ by *Quaternionic Geometry*; the conjugation of the imaginary quaternions commutes with the action of $Sp(1)$ because $Sp(1)$ is the unit group of the division algebra and the conjugation is inner, $q\lambda q^{-1}=\bar\lambda$ for $\lambda$ imaginary and $q$ unit; hence the antipodal involution of the fibres is independent of the trivialisation. The Obata connection preserves $\mathcal{Q}$ and is unique, and it preserves the conjugation because the latter is defined by the algebra and commutes with the structure group.

**Remark (the bundle of conjugate structures).** The conjugate structure is not a second quaternionic structure on $M$ in the sense of a distinguished subbundle of $\mathcal{Q}$ of rank three; it is the conjugate module structure, that is the same real bundle with the conjugated quaternionic scalars. The two coincide only over the points where a quaternionic-linear identification of $V$ with $\bar V$ exists, and a global such identification is a real structure of the quaternionic bundle, which need not exist.

## The Quaternionic Kähler Case

**Definition.** A quaternionic Kähler manifold is an almost quaternionic Riemannian manifold whose Levi-Civita connection preserves $\mathcal{Q}$; equivalently the holonomy lies in $Sp(n)\cdot Sp(1)$. Its fundamental four-form is

$$
\Omega = \omega_1\wedge\omega_1+\omega_2\wedge\omega_2+\omega_3\wedge\omega_3 ,
$$

where $\omega_i(X,Y)=g(J_iX,Y)$ and $J_1,J_2,J_3$ is a local quaternionic triple.

**Proposition.** The four-form $\Omega$ is well defined independently of the local triple, it is parallel for the Levi-Civita connection, and it is **invariant under the conjugate structure**; the class of the quaternionic Kähler metric is preserved by the conjugation, and the scalar curvature is invariant.

**Proof.** A change of the local triple is by an element of $Sp(1)$ acting on the imaginary quaternions by the adjoint action, and $\sum_i\omega_i\wedge\omega_i$ is the $Sp(1)$-invariant quadratic form of the three two-forms, so $\Omega$ is independent of the triple; it is parallel because the $\omega_i$ are parallel, by the preservation of $\mathcal{Q}$; the conjugation sends $\omega_i\mapsto-\omega_i$, hence $\omega_i\wedge\omega_i\mapsto\omega_i\wedge\omega_i$ and $\Omega$ is fixed; the metric and the Levi-Civita connection are untouched by the conjugation of the structure bundle, so the curvature data and the scalar curvature are invariant.

**Corollary.** On a quaternionic Kähler manifold the conjugation is an isometry of the total space of the structure bundle $\mathcal{Q}$ acting fibrewise on the sphere, and its quotient identifies antipodal compatible complex structures; in dimension at least eight, where the metric is Einstein by *Quaternionic Geometry*, the Einstein constant is conjugation-invariant.

**Proof.** The conjugation acts on each fibre by an isometry of the metric induced from $g$, and the statements on the curvature follow from the invariance of the metric; the Einstein property is that of *Quaternionic Geometry*, and its constant is built from the invariant metric.

## Worked Cases

### The Quaternionic Projective Space

For $\mathbb{HP}^n$ with the Fubini–Study quaternionic Kähler metric, the conjugation of the structure bundle is induced by the conjugation of the quaternion scalars; the fundamental four-form $\Omega$ is the invariant four-form of the symmetric space, and the conjugate structure is the antipode of the $\mathbb{CP}^1$-family of compatible complex structures over each point, those of the twistor fibration.

### The Flat Quaternionic Space

For $\mathbb{H}^n$ with the flat metric the triple $J_1,J_2,J_3$ is constant, the conjugation $J_i\mapsto-J_i$ is a constant bundle involution, and both the structure and its conjugate are parallel; the four-form $\Omega$ is the sum of three constant Kähler forms.

### The Four-Sphere

For $S^4=\mathbb{HP}^1$ the quotient identifies the antipodal compatible complex structures on each tangent space; the conjugation pairs $J$ with $-J$, and the pair is the fibre of the twistor fibration over the point, which is the two-sphere of complex structures.

## Summary

The **conjugation** of the quaternion algebra fixes the scalars and negates the imaginary part and acts on the sphere of compatible complex structures of a quaternionic structure by the antipode $J\mapsto-J$; on a quaternionic vector space it produces the **conjugate quaternionic vector space** $\bar V$ with $\bar J_i=-J_i$, an involution of the set of structures that is free. On an almost quaternionic manifold the conjugation is the bundle involution $\sigma(J)=-J$ of the structure bundle $\mathcal{Q}$; it is independent of the local quaternionic triple, commutes with $Sp(1)$, and is parallel for the Obata connection on a quaternionic manifold. In the **quaternionic Kähler case** the fundamental four-form $\Omega=\sum_i\omega_i\wedge\omega_i$ is parallel and invariant under the conjugation, and the metric, the Levi-Civita connection and the scalar curvature are conjugation-invariant. The structure itself is *Quaternionic Geometry*; the hyperkähler and twistor cases are *Hyperkähler Manifolds and the Twistor Space*; and the operators built from the conjugation belong to the `- * Operator Theory` group of the category.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\lambda\mapsto\bar\lambda$ | Conjugation of the quaternion algebra |
| $\mathcal{Q}$ | Rank-three bundle of compatible complex structures |
| $\sigma(J)=-J$ | Conjugate structure; bundle involution of $\mathcal{Q}$ |
| $\bar V$, $\bar J_i=-J_i$ | Conjugate quaternionic vector space and structure |
| $I_{(a,b,c)}=aJ_1+bJ_2+cJ_3$ | Sphere of compatible complex structures |
| $J\mapsto-J$ on $S^2$ | The antipodal action of the conjugation |
| $\omega_i(X,Y)=g(J_iX,Y)$ | Fundamental forms of a local triple |
| $\Omega=\sum_i\omega_i\wedge\omega_i$ | Fundamental four-form; conjugation-invariant |

## Further Reading

- Simon Salamon, "Quaternionic Kähler Manifolds", *Inventiones Mathematicae* 67 (1982), 143–171, for the quaternionic Kähler condition, the holonomy $Sp(n)\cdot Sp(1)$ and the fundamental four-form.
- Arthur L. Besse, *Einstein Manifolds* (Springer, 1987), for the quaternionic Kähler manifolds, the invariant forms and the twistor fibration.
- Dmitri V. Alekseevsky and Vicente Cortés, "Classification of Stationary Compact Homogeneous Quaternionic Kähler Manifolds", *Journal of the European Mathematical Society* 7 (2005), 315–347, for the classification side of the quaternionic Kähler structures.
- Shoshichi Kobayashi and Katsumi Nomizu, *Foundations of Differential Geometry*, Volume II (Interscience, 1969), for the structure bundles and their canonical connections.
