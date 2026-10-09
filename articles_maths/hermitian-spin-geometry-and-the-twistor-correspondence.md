
# __Hermitian Spin Geometry and the Twistor Correspondence__

## Introduction

**Hermitian spin geometry** is the spin geometry of a spinor bundle with a positive definite Hermitian form $h$ and the conjugation it defines; the conjugation is the charge conjugation of the spin representation, and it is the reality structure of the whole twistor construction. The **twistor correspondence** is the equivalence between the conformal geometry of a four-dimensional anti-self-dual manifold $M$ and the complex geometry of its twistor space $Z(M)$: points of $M$ correspond to rational curves in $Z(M)$ of a fixed normal type, and the fields on $M$ that satisfy the massless field equations correspond to cohomology classes on $Z(M)$. This article presents the correspondence and the **Penrose transform** in their structural form, with the Hermitian form as the datum that makes the reality conditions precise.

The two directions of the correspondence are the following. From the manifold to the twistor space, each point $x$ gives the curve $\pi^{-1}(x)\cong\mathbb{CP}^1$ with normal bundle $\mathcal{O}(1)\oplus\mathcal{O}(1)$, and the conformal structure of $M$ is recovered from the family of curves; this is the content of *Twistor Spaces and the Hermitian Structure of a Conformal Manifold*. From the twistor space to the manifold, a holomorphic object on $Z$ restricts to each curve and produces a field on $M$; the restriction defines the transform, and the Hermitian form is what turns complex-linear data into fields with reality conditions.

**The boundaries.** The twistor space and its real, complex and Hermitian structures are *Twistor Spaces and the Hermitian Structure of a Conformal Manifold*; the twistor operator and the twistor equation are *The Twistor Operator* and *The Penrose Operator*; the spinor bundle, the chirality and the charge conjugation are *Spin Geometry*; the complex analysis of the transform, the cohomology of the sheaves and the massless field equations are the referenced twistor literature. The body is a four-dimensional oriented spin manifold with an anti-self-dual conformal structure.

## Hermitian Spin Geometry

**Definition.** A **Hermitian spin structure** on a spin manifold is a positive definite Hermitian form $h$ on the spinor bundle $\mathcal{S}$ with respect to which the Clifford multiplication is skew, $c(v)^*=-c(v)$, together with the induced conjugation $\kappa : \mathcal{S}\to\bar{\mathcal{S}}$ of the spin representation. The form $h$ is the fibre form of the earlier articles, and the conjugation is the reality structure.

**Proposition.** The conjugation $\kappa$ is anti-linear, it commutes with the Clifford multiplication up to the complex conjugation of the Clifford coefficients, $\kappa(c(v)\sigma)=\overline{\text{coeff}}\,\kappa(\sigma)$, it is compatible with the chirality in the even-dimensional case, and it descends to a free anti-holomorphic involution $\sigma$ of the twistor space $Z(M)=\mathbb{P}(\mathcal{S}^-)$, the real structure of the previous article.

**Proof.** The conjugation of a Hermitian vector space with respect to a form is anti-linear and involutive; its compatibility with the Clifford action is the statement that $h$ is invariant under the structure group, and the action of $c(v)$ on the conjugate is the complex conjugate of the action on the original; the descent to the projectivisation is the definition of $\sigma$. The identification with the charge conjugation is the standard spinorial reality structure quoted from *Spin Geometry*.

**Remark (reality conditions).** The conjugation is the datum that lets one speak of real fields, of real cohomology classes, and of the Hermitian form on the coefficients of the cohomology; without it the twistor correspondence is a statement about complex data only. This is the sense in which the geometry of the correspondence is Hermitian.

## The Twistor Correspondence

**Theorem (the correspondence, quoted).** Let $(M,[g])$ be a four-dimensional anti-self-dual conformal spin manifold with twistor space $Z(M)$. Then:

**(a)** each point $x\in M$ determines a holomorphic rational curve $L_x=\pi^{-1}(x)$ in $Z(M)$ with normal bundle $\mathcal{O}(1)\oplus\mathcal{O}(1)$;

**(b)** conversely a holomorphic rational curve with normal bundle $\mathcal{O}(1)\oplus\mathcal{O}(1)$ in $Z(M)$ determines a point of $M$, and the two constructions are inverse;

**(c)** two points $x,y$ are null-separated with respect to the conformal structure exactly when the corresponding curves intersect;

**(d)** the complex structure of $Z(M)$ determines and is determined by the conformal structure of $M$.

**Proof sketch.** The curves are the fibres of the twistor projection; the normal bundle computation is the standard computation with the horizontal distribution and the fibrewise tangent bundle; the incidence condition is read from the conformal structure through the spinor parallelism that identifies the curve $L_x$. The statements are the theorems of Atiyah–Hitchin–Singer, quoted; the relevant complex structure is that of *Twistor Spaces and the Hermitian Structure of a Conformal Manifold*.

**Remark (the conformal structure from the curves).** Part (c) is the reason the family of curves encodes the conformal structure: the null separation of points is the incidence of curves, and a conformal structure is determined by its null cones. The twistor space therefore carries the conformal information in the complex-geometric arrangement of its curves, and the Hermitian form records the real points among them.

## The Penrose Transform

**Theorem (the transform, quoted).** Let $\mathcal{O}(k)$ be the pullback to $Z(M)$ of the hyperplane bundle of the fibre and let $\mathcal{F}$ be a holomorphic vector bundle on $Z(M)$; the **Penrose transform** is the map from the holomorphic cohomology on $Z(M)$ to the fields on $M$,

$$
\mathbb{H}^1(Z(M),\mathcal{O}(k)\otimes\mathcal{F}) \longrightarrow \{\text{massless fields on } M \text{ of the corresponding type}\} ,
$$

sending a cohomology class to the family of its restrictions to the twistor lines; it is an isomorphism onto the kernel of the relevant field equation, and the Hermitian form gives the reality conditions under which the image consists of real fields.

**Proof sketch.** The restrictions of a cohomology class to the lines $L_x$ vary holomorphically in $x$ and satisfy the field equation because of the incidence structure; the converse uses the cohomology of the projective line with values in $\mathcal{O}(k)\otimes\mathcal{F}$ and the fact that the family of lines is a complete family. The analytic details, the exact cohomology degrees and the field equations are the Penrose transform of the literature, quoted; the article records the structural form and the place of the Hermitian form in it.

**Remark (the twistor spinors).** The twistor equation of *The Penrose Operator* is the linearised form of the correspondence: a twistor spinor on $M$ corresponds to a holomorphic section of the appropriate bundle over $Z(M)$, and the twistor operator is the differential operator whose kernel is the image of the transform at the spinor level. The correspondence of the twistor space and the operator are thus two faces of the same Hermitian spin geometry.

## Summary

**Hermitian spin geometry** is spin geometry with a positive definite Hermitian form $h$ on the spinor bundle and the conjugation $\kappa$ it defines; the Clifford multiplication is skew for $h$, and the conjugation descends to the free anti-holomorphic **real structure** $\sigma$ of the twistor space, which fixes the reality conditions of the correspondence. The **twistor correspondence** identifies the points of a four-dimensional anti-self-dual conformal manifold with the holomorphic rational curves of $Z(M)$ having normal bundle $\mathcal{O}(1)\oplus\mathcal{O}(1)$, and encodes the conformal structure in the incidence of the curves. The **Penrose transform** is the isomorphism from the appropriate holomorphic cohomology on $Z(M)$ to the massless fields on $M$, obtained by restriction to the twistor lines, with the Hermitian form supplying the reality conditions; the twistor operator of *The Penrose Operator* is its spinor-level differential form. The object $Z(M)$ is *Twistor Spaces and the Hermitian Structure of a Conformal Manifold*, its complex and Hermitian structures are those of *Twistor Spaces and the Hermitian Structure of a Conformal Manifold*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $h$ on $\mathcal{S}$ | Hermitian fibre form; $c(v)^*=-c(v)$ |
| $\kappa$ | Charge conjugation; anti-linear reality structure |
| $\sigma$ | Real structure of $Z(M)$ induced by $\kappa$ |
| $L_x=\pi^{-1}(x)$ | Twistor line; normal bundle $\mathcal{O}(1)\oplus\mathcal{O}(1)$ |
| Incidence of $L_x,L_y$ | Null separation of $x,y$ in the conformal structure |
| $\mathbb{H}^1(Z,\mathcal{O}(k)\otimes\mathcal{F})$ | Cohomology source of the Penrose transform |
| Massless fields | Image of the transform; kernel of the field equation |

## Further Reading

- Roger Penrose, "Twistor Algebra", *Journal of Mathematical Physics* 8 (1967), 345–366, and Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time, Volume 2* (Cambridge University Press, 1986), for the twistor correspondence and the Penrose transform.
- Michael F. Atiyah, Nigel J. Hitchin and Isidore M. Singer, "Self-Duality in Four-Dimensional Riemannian Geometry", *Proceedings of the Royal Society of London A* 362 (1978), 425–461, for the twistor space, the normal bundle and the real structure.
- Michael G. Eastwood, "The Penrose Transform", in *Twistors in Mathematics and Physics*, London Mathematical Society Lecture Note Series 156 (Cambridge University Press, 1990), for the cohomological form of the transform.
- R. S. Ward and Raymond O. Wells, *Twistor Geometry and Field Theory* (Cambridge University Press, 1990), for the massless field equations and their twistor solutions.
