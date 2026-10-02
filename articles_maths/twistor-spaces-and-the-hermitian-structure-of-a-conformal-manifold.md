
# __Twistor Spaces and the Hermitian Structure of a Conformal Manifold__

## Introduction

The twistor space of a four-dimensional oriented conformal manifold is the projectivised negative spinor bundle,

$$
Z(M) = \mathbb{P}(\mathcal{S}^-) \longrightarrow M ,
$$

a bundle of projective lines whose fibre at $x$ is the sphere of complex structures on the tangent space $T_xM$ compatible with the conformal structure and the orientation. It is the complex-geometric object attached to the conformal class: the projection is holomorphic when the conformal structure is anti-self-dual, the fibres are holomorphic rational curves, and the conformal geometry of $M$ is encoded in the complex geometry of $Z(M)$. This article treats the twistor space as an object with structure — a fibration, a real structure, and a fibrewise Hermitian form — and leaves the complex structure to *The Complex Structure of the Twistor Space* and the metric to *The Hermitian Structure of the Twistor Space*.

The Hermitian content is the fibrewise form and the real structure it carries. Each fibre $\pi^{-1}(x)\cong\mathbb{CP}^1$ is a complex projective line with its Fubini–Study form, the antipodal map of the fibre is the restriction of a global anti-holomorphic involution $\sigma$ of $Z(M)$ without fixed points, and $\sigma$ is the real structure of the twistor space; the fixed loci of $\sigma$ are the twistor lines $\pi^{-1}(x)$, whose normal bundle is $\mathcal{O}(1)\oplus\mathcal{O}(1)$. The conformal structure of $M$ is recovered from the family of these curves, and the Hermitian form on $\mathcal{S}^-$ that defines the real structure is the fibre form of the spinor bundle with its conjugation.

**The boundaries.** The spinor bundle, its chirality and the fibre form are *Spin Geometry*; the twistor operator and the twistor equation are *The Twistor Operator* and *The Penrose Operator*; the complex structure, the Hermitian structure and the correspondence are the sibling `- * Theory` articles. The body is a four-dimensional oriented Riemannian manifold with a spin structure, $c(v)^2=-g(v,v)\operatorname{id}$, and the spinor bundle $\mathcal{S}=\mathcal{S}^+\oplus\mathcal{S}^-$.

## The Twistor Fibration

**Definition.** The **twistor space** of $(M,[g])$ is $Z(M)=\mathbb{P}(\mathcal{S}^-)$, the projectivisation of the negative spinor bundle; the **twistor projection** is $\pi : Z(M)\to M$, sending a line in $\mathcal{S}^-_x$ to the point $x$.

**Proposition.** The fibre $\pi^{-1}(x)$ is the set of complex structures on $T_xM$ compatible with $[g]$ and the orientation, a copy of $\mathbb{CP}^1$; the twistor projection is a fibre bundle with structure group $U(2)$ containing the fibrewise Möbius transformations; and a connection on $\mathcal{S}^-$ (the spin connection of any metric in the conformal class) gives a horizontal distribution on $Z(M)$.

**Proof.** A compatible complex structure on $T_xM$ is an endomorphism $J$ with $J^2=-\operatorname{id}$ preserving $g$ and the orientation; the set of such $J$ is the homogeneous space $SO(4)/U(2)$, which is $\mathbb{CP}^1$; a complex structure acts on $\mathcal{S}^-_x$ by Clifford multiplication with eigenvalue $i$ on a line, so the set of them is the projectivisation of the two-dimensional complex spinor space $\mathcal{S}^-_x$. The horizontal distribution is the horizontal lift of the Levi-Civita connection of a representative metric, and the replacement of the metric by a conformally equivalent one changes the distribution by a horizontal tensor but not the underlying conformal structure.

**Remark (the four-dimensional restriction).** The twistor space is built from the negative half of the spinor bundle because in dimension four the Hodge star acts on the two-forms and splits the Weyl tensor into self-dual and anti-self-dual parts; the choice of $\mathcal{S}^-$ selects one orientation, and the other choice gives the conjugate twistor space. In higher dimension the analogue is the twistor space of a quaternionic or quaternionic Kähler manifold, which is *Quaternionic Geometry*.

## The Hermitian Structure

**Definition.** The **real structure** of the twistor space is the anti-holomorphic involution $\sigma : Z(M)\to Z(M)$ induced by the conjugation of the spinor bundle $\mathcal{S}^-$ with respect to the fibre form $h$; the **fibrewise Hermitian form** is the pullback to each fibre of the Fubini–Study form of the projective line.

**Proposition.** The real structure $\sigma$ is well defined, it restricts on each fibre to the antipode of $\mathbb{CP}^1$, it has no fixed points, and its fixed "curves" are the twistor lines: $\sigma$ maps the fibre $\pi^{-1}(x)$ to itself with no fixed line, and the twistor lines are the maximally real families. The conjugation on $\mathcal{S}^-$ is the charge conjugation twisted by the chirality, and the Hermitian form $h$ is its reference form.

**Proof.** The fibre form $h$ is a positive definite Hermitian form on $\mathcal{S}^-$, and the choice of a conjugation of the complex vector space with respect to $h$ determines a projective anti-linear map of $\mathbb P(\mathcal{S}^-)$, the antipode on each fibre; the antipodal map of $\mathbb{CP}^1$ has no fixed point, so $\sigma$ is free on the fibres. The identification with the charge conjugation is the standard form of the real structure on the spinor bundle, quoted from *Spin Geometry*.

**Remark (the Hermitian form and the Kähler question).** The fibrewise Hermitian form is natural, but it does not extend to a Kähler form on $Z(M)$ in general: the twistor space of a self-dual conformal manifold is Kähler only under additional hypotheses, and the natural object is the **Hermitian structure** — a complex structure together with a Hermitian metric — rather than a Kähler one. The metric properties are *The Hermitian Structure of the Twistor Space*, where the Bers–Salamon and related forms are the subject; no Kähler claim is made here.

**Remark (the Hermitian structure as a family of complex structures).** A second reading of "Hermitian" is the family: the twistor space parametrises the compatible complex structures of $M$, one sphere's worth at each point, and the Hermitian structure of the conformal manifold is this family. For a hyperkähler manifold the family is a full $\mathbb{CP}^1$ of compatible complex structures and the twistor space carries a holomorphic symplectic form; this is *Hyperkähler Manifolds and the Twistor Space*.

## Worked Cases

### The Four-Sphere

For $S^4$ with the round conformal structure the spinor bundle is the fundamental representation, and the twistor space is the complex projective space $\mathbb{CP}^3$ with the Fubini–Study form; the real structure is the antipodal-type involution, the twistor lines are the $\mathbb{CP}^1$'s of the standard linear family, and the self-dual conformal structures of $\mathbb{CP}^3$ with these lines are the LeBrun and Penrose constructions.

### The Complex Projective Plane

For $\mathbb{CP}^2$ with the Fubini–Study orientation, the twistor space is a complex threefold of a different kind, and the twistor fibration is the bundle of the standard $\mathbb{CP}^1$-family; the example shows that the twistor space can be a projective variety, not only a bundle over a non-algebraic base.

### A Conformal Compactification

For the conformal compactification of flat space, the twistor space is the complex projective variety of the flat model, and the twistor lines are the real lines of the projective primed spinor space; the flat case is the model on which the Penrose transform is computed and the curved cases are deformations of it.

## Summary

The **twistor space** $Z(M)=\mathbb{P}(\mathcal{S}^-)$ of a four-dimensional oriented conformal manifold is a bundle of projective lines over $M$; the fibre $\pi^{-1}(x)$ is the sphere of compatible complex structures, a $\mathbb{CP}^1$, and the **twistor projection** is a fibre bundle with a horizontal distribution from the spin connection. The space carries a **real structure** $\sigma$, the anti-holomorphic involution induced by the conjugation of the spinor bundle, restricting on each fibre to the antipode and having no fixed points; its fixed curves, the twistor lines, have normal bundle $\mathcal{O}(1)\oplus\mathcal{O}(1)$. The fibrewise **Hermitian form** is the Fubini–Study form of the fibre, and it is a Hermitian structure, not a Kähler one, in general. The twistor space is complex exactly when the conformal structure is anti-self-dual, which is *The Complex Structure of the Twistor Space*; the metric forms are *The Hermitian Structure of the Twistor Space*; and the correspondence with the fields on $M$ is *Hermitian Spin Geometry and the Twistor Correspondence*. For $S^4$ the twistor space is $\mathbb{CP}^3$ with the Fubini–Study form.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $Z(M)=\mathbb{P}(\mathcal{S}^-)$ | Twistor space |
| $\pi : Z(M)\to M$ | Twistor projection |
| $\pi^{-1}(x)\cong\mathbb{CP}^1$ | Fibre; sphere of compatible complex structures |
| $\mathcal{O}(1)\oplus\mathcal{O}(1)$ | Normal bundle of a twistor line |
| $\sigma$ | Real structure; antipodal on each fibre, no fixed points |
| $h$ on $\mathcal{S}^-$ | Fibre form defining the real structure |
| Kähler condition | Not assumed; the natural object is Hermitian |
| $Z(S^4)=\mathbb{CP}^3$ | The model case |

## Further Reading

- Michael F. Atiyah, Nigel J. Hitchin and Isidore M. Singer, "Self-Duality in Four-Dimensional Riemannian Geometry", *Proceedings of the Royal Society of London A* 362 (1978), 425–461, for the twistor space, the real structure and the twistor lines.
- Nigel J. Hitchin, "Kählerian Twistor Spaces", *Proceedings of the London Mathematical Society* 43 (1981), 133–150, for the Hermitian and Kähler structures on twistor spaces.
- Simon Salamon, "Quaternionic Kähler Manifolds", *Inventiones Mathematicae* 67 (1982), 143–171, for the higher-dimensional twistor space and its Hermitian structure.
- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time, Volume 2* (Cambridge University Press, 1986), for the twistor space of the conformal compactification and the spinor form.
