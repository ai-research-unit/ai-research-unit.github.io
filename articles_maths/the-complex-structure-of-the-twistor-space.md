
# __The Complex Structure of the Twistor Space__

## Introduction

The twistor space $Z(M)=\mathbb{P}(\mathcal{S}^-)$ of a four-dimensional oriented conformal spin manifold carries a natural **almost complex structure** $I$, built from the horizontal distribution of the Levi-Civita connection of a metric in the conformal class and the complex structure of the projective fibre. The almost complex structure is conformally natural; its **integrability** is the geometric theorem that ties the twistor space to the curvature of the manifold: $I$ is integrable if and only if the metric is **anti-self-dual**, that is the anti-self-dual part $W^-$ of the Weyl tensor vanishes. When it is integrable, the twistor projection is holomorphic, the twistor lines are holomorphic rational curves, and the complex geometry of $Z(M)$ is equivalent to the conformal geometry of $M$.

**The boundaries.** The twistor space and its real and Hermitian structures are *Twistor Spaces and the Hermitian Structure of a Conformal Manifold* and *The Hermitian Structure of the Twistor Space*; the correspondence and the transform are *Hermitian Spin Geometry and the Twistor Correspondence*; the spinor bundle and the chirality are *Spin Geometry*; the Weyl tensor and the Levi-Civita connection are *Riemannian Geometry* and *Fibre Bundles, Connections and Curvature*. The body is a four-dimensional oriented conformal spin manifold $(M,[g])$ with the choice of the negative spinor bundle.

## The Almost Complex Structure

**Definition.** Let $g$ be a representative metric in the conformal class, let $H$ be the horizontal distribution of its Levi-Civita connection on the fibre bundle $\pi : Z(M)\to M$, and let $J^{\mathrm{fib}}$ be the complex structure of the projective fibre $\mathbb{CP}^1$. The **almost complex structure** of the twistor space is

$$
I = J^{H}\oplus J^{\mathrm{fib}} ,
$$

acting by the lift of the complex structure $J^{H}$ on the horizontal space $H\cong\pi^*TM$ (induced by the fibrewise complex structure of the twistor point) and by $J^{\mathrm{fib}}$ on the vertical space.

**Proposition.** The almost complex structure $I$ is well defined, it is compatible with the orientation, the twistor projection $\pi$ is $(I,J^{H})$-holomorphic in the sense that its differential is complex-linear on $H$, and $I$ restricts on each fibre to the standard complex structure of $\mathbb{CP}^1$; the fibrewise complex structure on $H$ is the one determined by the twistor point, that is by the complex structure on $T_xM$ which that point represents.

**Proof.** The horizontal distribution is a complement to the vertical space; a twistor point over $x$ is a compatible complex structure on $T_xM$, which is an endomorphism of the horizontal space with square $-\operatorname{id}$ on the two-dimensional quotient structure; combining with the fibrewise structure gives an endomorphism $I$ of the tangent space of $Z(M)$ with $I^2=-\operatorname{id}$, and the compatibility with the orientation follows from the compatibility of the twistor point with the orientation. The restriction to the fibre is by construction the complex structure of $\mathbb{CP}^1$.

**Remark (the two orientation choices).** The construction uses the negative spinor bundle $\mathcal{S}^-$, one of the two chiral halves; the other choice gives the conjugate almost complex structure and the criterion with the other half $W^+$ of the Weyl tensor. The article fixes one choice and states the criterion for it; the mirror statements are obtained by reversing the orientation of $M$.

## Integrability

**Theorem (the integrability criterion, quoted).** The almost complex structure $I$ of the twistor space is **integrable** if and only if the metric $g$ is **anti-self-dual**, $W^-=0$. When $W^-=0$ the twistor space is a complex threefold, the projection $\pi$ is holomorphic, and each twistor line $\pi^{-1}(x)$ is a holomorphic rational curve with normal bundle $\mathcal{O}(1)\oplus\mathcal{O}(1)$.

**Proof sketch.** The Nijenhuis tensor of $I$ is computed on the horizontal and vertical parts; the vertical and mixed components vanish identically, and the horizontal component is a tensor on $M$ that is identified with the anti-self-dual Weyl tensor $W^-$ up to a non-zero constant depending on the dimension, so the vanishing of the Nijenhuis tensor is equivalent to $W^-=0$. The identification is the computation of Atiyah–Hitchin–Singer, quoted; the integrability is then the Newlander–Nirenberg theorem, and the holomorphicity of the projection and of the lines follows from the definition of $I$.

**Remark (the two halves of the Weyl tensor).** In dimension four the Weyl tensor splits as $W=W^++W^-$ under the Hodge star of the two-forms, and the two halves are exchanged by the reversal of the orientation; the twistor space of a given orientation is complex exactly when the half of the Weyl tensor selected by that orientation vanishes. The self-dual and anti-self-dual conditions are therefore the two faces of the same construction, and the article works with one of them.

**Corollary (the Einstein case).** If $M$ is Einstein and anti-self-dual, the twistor space is a complex threefold with a real structure and the Hermitian form of *The Hermitian Structure of the Twistor Space*; in particular the model case $S^4$ gives the complex projective space $\mathbb{CP}^3$.

**Proof.** An Einstein anti-self-dual metric satisfies the hypotheses of the theorem; the additional structures are those of the cited articles, and the model case is the explicit computation.

## Dependence on the Conformal Class

**Proposition.** The almost complex structure $I$ depends only on the conformal class and the orientation: a conformal change $g\to\Omega^2g$ changes the horizontal distribution by a horizontal tensor field but leaves the horizontal complex structure and the vertical structure unchanged, so $I$ is the same.

**Proof.** The Levi-Civita connections of two conformally related metrics differ by a horizontal tensor, the difference being expressible in terms of the differential of the conformal factor; the horizontal complement $H$ of the vertical space changes, but the complex structure induced on the horizontal space by the twistor point is defined by the conformal class, since a compatible complex structure depends only on the conformal class and the orientation. Hence $I$ is conformally invariant.

**Remark (why the twistor space can encode the conformal geometry).** The conformal invariance of $I$ is the reason the twistor space is a conformal object: the complex structure of $Z(M)$ depends on the conformal class and not on the metric, while the metric in the class selects a horizontal distribution. The Hermitian form of *The Hermitian Structure of the Twistor Space* depends on the representative metric only through the scaling, in accordance with this invariance.

## Summary

The **almost complex structure** of the twistor space is $I=J^H\oplus J^{\mathrm{fib}}$, the sum of the horizontal complex structure induced by the twistor point and the standard complex structure of the fibre $\mathbb{CP}^1$; the projection is holomorphic on the horizontal part and $I$ restricts to the standard structure on each fibre. It is **integrable exactly when the metric is anti-self-dual**, $W^-=0$, by the computation of the Nijenhuis tensor and the Newlander–Nirenberg theorem; then $Z(M)$ is a complex threefold, the twistor lines are holomorphic rational curves with normal bundle $\mathcal{O}(1)\oplus\mathcal{O}(1)$, and in the Einstein case the twistor space carries the Hermitian structure of the sibling article. The almost complex structure depends only on the **conformal class and the orientation**, which is the reason the twistor space is a conformal object. The twistor space itself is *Twistor Spaces and the Hermitian Structure of a Conformal Manifold*, the metric side is *The Hermitian Structure of the Twistor Space*, the correspondence is *Hermitian Spin Geometry and the Twistor Correspondence*, and the criterion is the theorem of Atiyah–Hitchin–Singer.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $Z(M)=\mathbb{P}(\mathcal{S}^-)$ | Twistor space |
| $H$ | Horizontal distribution of the Levi-Civita connection |
| $J^{\mathrm{fib}}$ | Standard complex structure of the fibre $\mathbb{CP}^1$ |
| $I=J^H\oplus J^{\mathrm{fib}}$ | Almost complex structure of $Z(M)$ |
| $W=W^++W^-$ | Weyl tensor and its two halves |
| $W^-=0$ | Anti-self-duality; integrability of $I$ |
| $\mathcal{O}(1)\oplus\mathcal{O}(1)$ | Normal bundle of a twistor line |
| $I$ independent of the metric in $[g]$ | Conformal invariance of the complex structure |

## Further Reading

- Michael F. Atiyah, Nigel J. Hitchin and Isidore M. Singer, "Self-Duality in Four-Dimensional Riemannian Geometry", *Proceedings of the Royal Society of London A* 362 (1978), 425–461, for the almost complex structure, its integrability and the anti-self-duality criterion.
- Nigel J. Hitchin, "Kählerian Twistor Spaces", *Proceedings of the London Mathematical Society* 43 (1981), 133–150, for the complex and Kähler structures on twistor spaces.
- Simon Salamon, "Quaternionic Kähler Manifolds", *Inventiones Mathematicae* 67 (1982), 143–171, for the higher-dimensional analogue of the integrability statement.
- Arthur L. Besse, *Einstein Manifolds* (Springer, 1987), for the Weyl tensor, the self-dual and anti-self-dual conditions and the twistor space of an Einstein four-manifold.
