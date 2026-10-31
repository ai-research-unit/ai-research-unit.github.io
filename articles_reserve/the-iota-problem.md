# __The Iota Problem: One Letter, Seventeen Objects__

## Introduction

The Greek letter $\iota$ is used 2,336 times in 196 articles of the mathematics and physics collections. It names seventeen different objects, plus one index label. The three uses that are usually noticed — the Clifford comparison $\iota_{\mathrm{Cl}}$, the interior product $\iota_X$, and the octonion units $\iota_1,\dots,\iota_7$ — are not the problem. The first two are stable because the subscript names the object. The third is confined to one article, but its form $\iota_i$ is also a coproduct inclusion elsewhere. The other fourteen are where the collisions live, and the forms they share are the damage.

A summary in circulation gives 166 uses of $\iota_{\mathrm{Cl}}$ in 9 files, 64 uses of the interior product, and “several articles” for the octonion units. The first figure is exact. The second is an undercount: the exact token $\iota_X$ occurs 71 times, and the interior product occurs 274 times once its variants are counted. The third is wrong: the octonion units occur 12 times, all in one article.

Two conventions govern the counts. They count occurrences, not lines and not articles. And a compound such as $\sigma\iota$ counts the inversion once, although the letter is doing the same work as in the standalone $\iota$.

No article defines the letter globally. The conventions articles fix $\iota_{\mathrm{Cl}}$ and the index subscript ${}_{\iota}$, not $\iota$ itself.

## The Count and the Screen

The scan reads every Markdown file in `articles_maths` and `articles_physics` and counts every control sequence `\iota` that is not part of a longer command name. Subscripts and superscripts are kept. The scan does not isolate math regions; it counts the control sequence wherever it appears.

The corpus contains 115 distinct spellings of the letter. Most occur once and belong to one object. The collisions are a small subset, and they are concentrated in the short forms: the bare letter, the subscript $u$, the letters $i,j,k$, and the numerals $1,2,3$.

| Object | Typical form | Occurrences | Articles |
|---|---|---:|---:|
| The inversion of a group | $\iota(g)=g^{-1}$ | 335 | 39 |
| The involutive anti-automorphism | $\iota(gh)=\iota(h)\iota(g)$ | 98 | 5 |
| The inner automorphism | $\iota_u(x)=uxu^{-1}$ | 169 | 21 |
| The quaternion involution | $\iota_\nu(q)=\nu q\nu^{-1}$ | 348 | 7 |
| The octonion imaginary units | $\iota_1,\dots,\iota_7$ | 12 | 1 |
| The interior product | $\iota_X\omega$ | 274 | 30 |
| The Clifford comparison | $\iota_{\mathrm{Cl}}$ | 167 | 9 |
| The canonical embedding | $\iota:X\to\widehat X$ | 666 | 76 |
| The fundamental class | $\iota_n\in H^n(K(\pi,n);\pi)$ | 27 | 2 |
| The involution of a space | $\iota(v)=-v$ | 69 | 3 |
| The angular velocity | $d\iota=\iota_1\vec e_x+\iota_2\vec e_y+\iota_3\vec e_z$ | 85 | 1 |
| The moving-frame map | $d\iota=2r^\dagger dr$ | 28 | 1 |
| The grade-two element | $\iota\in\mathbb{G}_2$ | 6 | 1 |
| The Newman–Penrose spinor | $\iota=(0,1)^T$ | 26 | 1 |
| The identity map | $\iota$ | 18 | 1 |
| The base type | $\iota$ | 5 | 1 |
| The algebra element | $\iota=1\otimes i$ | 2 | 1 |

One further occurrence, in the index table, is the label ${}_{\iota}$; it is not an object, and it is treated separately below.

Each object section lists the ten largest sources; the heading gives the full count and the full number of articles.

The canonical embedding is one object with four constructions. Its 666 occurrences in 76 articles are separated in the body, because the four kinds are repaired differently.

Two figures need a comment. The exact token $\iota_X$ occurs 71 times; the interior product occurs 274 times. The difference is the variants: $\iota_x$, $\iota_\eta$, $\iota_{e_i}$, $\iota_R$, $\iota_{\partial/\partial z^j}$, and the contractions written inside Clifford multiplication. The exact token $\iota_{\mathrm{Cl}}$ occurs 166 times; the object occurs 167 times, because one Dirac article writes the complexified extension of the comparison as bare $\iota$.

## The Objects


### The inversion of a group — 335 occurrences in 39 articles

The inversion of a group is the map $\iota(g)=g^{-1}$. It is an anti-automorphism, $\iota(gh)=\iota(h)\iota(g)$, and an involution, $\iota^2=\mathrm{id}$. The involutive-group articles compose it with an involution $\sigma$: $\alpha=\sigma\iota$ is an automorphism, and $\sigma=\iota\alpha$ is the same statement solved for $\sigma$. The letter appears in both the inversion and the composite, but in the composite it is still the inversion.

The 335 occurrences are the third largest object, after the canonical embedding (666) and the quaternion involution (348). One article supplies 78 of them; the operator-layer article supplies 36.

| Article | Occurrences |
|---|---:|
| [Involutive Groups](../articles_maths/involutive-groups.html) | 78 |
| [Involutions on the Operator Layer](../articles_maths/involutions-on-the-operator-layer.html) | 36 |
| [Involutive Topological Groups](../articles_maths/involutive-topological-groups.html) | 27 |
| [The Group Inversion as an Adjoint](../articles_maths/the-group-inversion-as-an-adjoint.html) | 22 |
| [Involutions and the Fixed-Point Subgroup](../articles_maths/involutions-and-the-fixed-point-subgroup.html) | 21 |
| [The Signed Adjoint of the Left Multiplication on a Group](../articles_maths/the-signed-adjoint-of-the-left-multiplication-on-a-group.html) | 16 |
| [The Involution on the Translation Operators](../articles_maths/the-involution-on-the-translation-operators.html) | 14 |
| [Free Involutions and the Quotient](../articles_maths/free-involutions-and-the-quotient.html) | 12 |
| [The Fixed-Point Subgroup of a Continuous Involution](../articles_maths/the-fixed-point-subgroup-of-a-continuous-involution.html) | 11 |
| [The Signed Adjoint of the Left Multiplication on a Topological Group](../articles_maths/the-signed-adjoint-of-the-left-multiplication-on-a-topological-group.html) | 8 |
| [The Centre of an Involutive Group](../articles_maths/the-centre-of-an-involutive-group.html) | 7 |
| [The Involution on the Enveloping Algebra of a Lie Group](../articles_maths/the-involution-on-the-enveloping-algebra-of-a-lie-group.html) | 7 |
| [The Signed Sandwich on a Topological Group](../articles_maths/the-signed-sandwich-on-a-topological-group.html) | 6 |
| [The Signed Adjoint of the Reflection on the Group Algebra](../articles_maths/the-signed-adjoint-of-the-reflection-on-the-group-algebra.html) | 5 |
| [The Signed Adjoint Sandwich on a Topological Group](../articles_maths/the-signed-adjoint-sandwich-on-a-topological-group.html) | 5 |
| [The Signed Sandwich on a Group](../articles_maths/the-signed-sandwich-on-a-group.html) | 5 |
| [Involutive Group Actions on a Space](../articles_maths/involutive-group-actions-on-a-space.html) | 4 |
| [Involutive Profinite Groups](../articles_maths/involutive-profinite-groups.html) | 4 |
| [Operators on a Topological Group](../articles_maths/operators-on-a-topological-group.html) | 4 |
| [The Adjoint of the Left Multiplication on a Topological Group](../articles_maths/the-adjoint-of-the-left-multiplication-on-a-topological-group.html) | 4 |
| [The Commuting Algebra of an Involution](../articles_maths/the-commuting-algebra-of-an-involution.html) | 4 |
| [The Signed Left Multiplication on a Topological Group](../articles_maths/the-signed-left-multiplication-on-a-topological-group.html) | 4 |
| [Complex Norm and Invertibility](../articles_maths/complex-norm-and-invertibility.html) | 3 |
| [Involutive Group Actions](../articles_maths/involutive-group-actions.html) | 3 |
| [Lie Groups](../articles_maths/lie-groups.html) | 3 |
| [Operators on a Lie Group](../articles_maths/operators-on-a-lie-group.html) | 3 |
| [Real Norm and Invertibility](../articles_maths/real-norm-and-invertibility.html) | 3 |
| [Reflections as Signed Two-Sided Operators on a Group](../articles_maths/reflections-as-signed-two-sided-operators-on-a-group.html) | 3 |
| [Involutions and Pontryagin Duality](../articles_maths/involutions-and-pontryagin-duality.html) | 2 |
| [Reflections as Signed Two-Sided Operators on a Topological Group](../articles_maths/reflections-as-signed-two-sided-operators-on-a-topological-group.html) | 2 |
| [Complex Exponential and Lie Group Structure](../articles_maths/complex-exponential-and-lie-group-structure.html) | 1 |
| [Involutive Compact Groups](../articles_maths/involutive-compact-groups.html) | 1 |
| [Real Polar Decomposition](../articles_maths/real-polar-decomposition.html) | 1 |
| [The Graded Action on a Module over a Topological Group](../articles_maths/the-graded-action-on-a-module-over-a-topological-group.html) | 1 |
| [The Graded Adjoint Action on a Module over a Topological Group](../articles_maths/the-graded-adjoint-action-on-a-module-over-a-topological-group.html) | 1 |
| [The Left and Right Regular Representation](../articles_maths/the-left-and-right-regular-representation.html) | 1 |
| [The Signed Adjoint of the Left Multiplication on the Group Algebra](../articles_maths/the-signed-adjoint-of-the-left-multiplication-on-the-group-algebra.html) | 1 |
| [The Signed Adjoint of the Reflection on a Topological Group](../articles_maths/the-signed-adjoint-of-the-reflection-on-a-topological-group.html) | 1 |
| [The Signed Left Multiplication on the Group Algebra](../articles_maths/the-signed-left-multiplication-on-the-group-algebra.html) | 1 |

### The involutive anti-automorphism — 98 occurrences in 5 articles

Here $\iota$ is an abstract anti-automorphism of order two, not the group inversion unless the group is abelian. The definition is $\iota(gh)=\iota(h)\iota(g)$ and $\iota^2=\mathrm{id}$. In the group ring it extends linearly from the inversion; in the Hecke algebra it is the ring involution that sends $q$ to $q^{-1}$ and $T_w$ to $(T_{w^{-1}})^*$; on the Riemann sphere it is complex conjugation. The path-algebra article uses it for the identification with the opposite algebra.

The object is distinct from the inversion because it need not come from a group element. The written form is the same, and only the surrounding algebra says which one is meant.

| Article | Occurrences |
|---|---:|
| [Involutions of a Group Ring](../articles_maths/involutions-of-a-group-ring.html) | 40 |
| [The Conjugate Symmetry of the Hecke Operator](../articles_maths/the-conjugate-symmetry-of-the-hecke-operator.html) | 33 |
| [The Involution on the Möbius Operators](../articles_maths/the-involution-on-the-mobius-operators.html) | 20 |
| [Hecke Algebras](../articles_maths/hecke-algebras.html) | 4 |
| [Involutions of a Path Algebra](../articles_maths/involutions-of-a-path-algebra.html) | 1 |

### The inner automorphism — 169 occurrences in 21 articles

The inner automorphism is $\iota_u(x)=uxu^{-1}$. It satisfies $\iota_u\circ\iota_v=\iota_{uv}$, $\iota_u^{-1}=\iota_{u^{-1}}$, and $\iota_1=\mathrm{id}$. On a Hilbert space the same letter is used for $\iota_U(T)=UTU^*$; on a $C^*$-algebra it is the same formula with the adjoint in place of the inverse.

The conjugation action and the sandwich operator are the same object in different notation. The article on the quaternioid as a complex vector space uses $\iota$ for the scalar action, which is the inner automorphism by a complex scalar.

| Article | Occurrences |
|---|---:|
| [Reflections as Signed Two-Sided Operators on an Algebra](../articles_maths/reflections-as-signed-two-sided-operators-on-an-algebra.html) | 24 |
| [Quaternion Automorphisms and Derivations](../articles_maths/quaternion-automorphisms-and-derivations.html) | 23 |
| [Automorphisms and Derivations of Algebras](../articles_maths/automorphisms-and-derivations-of-algebras.html) | 22 |
| [Split-Quaternion Automorphisms and Derivations](../articles_maths/split-quaternion-automorphisms-and-derivations.html) | 15 |
| [Biquaternion Automorphisms and Derivations](../articles_maths/biquaternion-automorphisms-and-derivations.html) | 12 |
| [The Generalised Hamilton–Rodrigues Calculus](../articles_maths/the-generalised-hamilton-rodrigues-calculus.html) | 9 |
| [The Signed Adjoint of the Reflection on a Hilbert Space](../articles_maths/the-signed-adjoint-of-the-reflection-on-a-hilbert-space.html) | 9 |
| [Unitary Operators](../articles_maths/unitary-operators.html) | 9 |
| [Reflections as Signed Two-Sided Operators on a Hilbert Space](../articles_maths/reflections-as-signed-two-sided-operators-on-a-hilbert-space.html) | 8 |
| [Quaternion Involutions and Projections](../articles_maths/quaternion-involutions-and-projections.html) | 7 |
| [The Sandwich Operator on an Algebra](../articles_maths/the-sandwich-operator-on-an-algebra.html) | 6 |
| [The Signed Sandwich on an Algebra](../articles_maths/the-signed-sandwich-on-an-algebra.html) | 6 |
| [Frobenius Algebras](../articles_maths/frobenius-algebras.html) | 5 |
| [The Quaternioid as a Vector Space over $\mathbb{C}$](../articles_maths/the-quaternioid-as-a-vector-space-over-c.html) | 5 |
| [Involutive Graded Algebras](../articles_maths/involutive-graded-algebras.html) | 3 |
| [Gauge Redundancy and the Information in the Gauge Orbit in Biquaternionic Form](../articles_physics/gauge-redundancy-and-the-information-in-the-gauge-orbit-in-biquaternionic-form.html) | 1 |
| [Split-Biquaternion Automorphisms and Derivations](../articles_maths/split-biquaternion-automorphisms-and-derivations.html) | 1 |
| [The Commutator Operator](../articles_maths/the-commutator-operator.html) | 1 |
| [The Signed Adjoint of the Reflection on an Algebra](../articles_maths/the-signed-adjoint-of-the-reflection-on-an-algebra.html) | 1 |
| [The Signed Adjoint Sandwich on an Algebra](../articles_maths/the-signed-adjoint-sandwich-on-an-algebra.html) | 1 |
| [The Signed Sandwich on a Hilbert Space](../articles_maths/the-signed-sandwich-on-a-hilbert-space.html) | 1 |

### The quaternion involution — 348 occurrences in 7 articles

The quaternion involution is $\iota_\nu(\tilde q)=\nu\tilde q\nu^{-1}$ for a unit imaginary $\nu$. Because $\nu^{-1}=-\nu$ for such a unit, the same map is $-\nu\tilde q\nu$. The coordinate maps $\iota_k$ are the cases $\nu=\vec e_k$, and the three of them generate the Klein four-group of involutions. The general axis $\nu$ gives the continuous family.

One statistics article supplies 138 of them. The object is the second largest in the corpus, and its notation is stable: the subscript always names the axis, even when the axis is a composite such as $\nu_1\times\nu_2$.

| Article | Occurrences |
|---|---:|
| [Quaternion Augmented Statistics](../articles_maths/quaternion-augmented-statistics.html) | 138 |
| [Quaternion Involutions and Projections](../articles_maths/quaternion-involutions-and-projections.html) | 90 |
| [The Group of Involutions of the Quaternioid](../articles_maths/the-group-of-involutions-of-the-quaternioid.html) | 70 |
| [The Generalised Hamilton–Rodrigues Calculus](../articles_maths/the-generalised-hamilton-rodrigues-calculus.html) | 26 |
| [Decompositions Along the Remarkable Subspaces of the Quaternions](../articles_maths/decompositions-along-the-remarkable-subspaces-of-the-quaternions.html) | 15 |
| [Comparison of the Remarkable Subspaces of the Quaternions](../articles_maths/comparison-of-the-remarkable-subspaces-of-the-quaternions.html) | 6 |
| [Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Quaternions](../articles_maths/introduction-to-the-2x2-matrix-element-representation-of-quaternions.html) | 3 |

### The octonion imaginary units — 12 occurrences in 1 article

The octonion units are the seven imaginary basis elements $\iota_1,\dots,\iota_7$, with $\iota_1=\vec e_x$, $\iota_2=\vec e_y$, $\iota_3=\vec e_z$ and the remaining four the associator directions. A general element is $u=u_0+\sum_{i=1}^{7}u_i\iota_i$. The subscript is a basis index, not the parameter of a map.

This is one of the few objects whose notation is confined to a single article. It still collides with the coproduct inclusions, which use the same $\iota_i$ in 7 occurrences elsewhere. Inside *Special and Exceptional Jordan Algebras* there is no ambiguity; outside it there is.

| Article | Occurrences |
|---|---:|
| [Special and Exceptional Jordan Algebras](../articles_maths/special-and-exceptional-jordan-algebras.html) | 12 |

### The interior product — 274 occurrences in 30 articles

The interior product is $(\iota_X\omega)(Y_1,\dots,Y_{k-1})=\omega(X,Y_1,\dots,Y_{k-1})$. The exact token $\iota_X$ occurs 71 times, in 8 articles. The object occurs 274 times in 30 articles, because the vector is also written $x$, $\eta$, $e_i$, $R$, $u$, or a coordinate derivative.

The variants are not a defect: $\iota_x$ and $\iota_X$ are the same operation, and the lower-case letter is the conventional way to distinguish a vector field from a multivector. The defect is that the same letter also names an inner automorphism with subscript $u$ and a canonical embedding with subscript $u$, so $\iota_u$ can be an interior product, a conjugation, or an order-unit map depending on the article.

| Article | Occurrences |
|---|---:|
| [The Lie Derivative](../articles_maths/the-lie-derivative.html) | 59 |
| [The Exterior Derivative](../articles_maths/the-exterior-derivative.html) | 49 |
| [The Exterior Derivative on the Lie Algebra](../articles_maths/the-exterior-derivative-on-the-lie-algebra.html) | 29 |
| [Symplectic Geometry](../articles_maths/symplectic-geometry.html) | 25 |
| [The Codifferential](../articles_maths/the-codifferential.html) | 14 |
| [Spin Representations and Clifford Modules with Inner Conjugation](../articles_maths/spin-representations-and-clifford-modules-with-inner-conjugation.html) | 12 |
| [The Flow Operator](../articles_maths/the-flow-operator.html) | 12 |
| [Contact Geometry](../articles_maths/contact-geometry.html) | 9 |
| [Lagrangian and Hamiltonian Systems](../articles_maths/lagrangian-and-hamiltonian-systems.html) | 9 |
| [Bounded Clifford Modules and the Continuous Spin Representation](../articles_maths/bounded-clifford-modules-and-the-continuous-spin-representation.html) | 6 |
| [Diffeomorphism Groups](../articles_maths/diffeomorphism-groups.html) | 6 |
| [Multisymplectic and Covariant Hamiltonian Field Theory](../articles_maths/multisymplectic-and-covariant-hamiltonian-field-theory.html) | 6 |
| [Symplectic and Contact Topology](../articles_maths/symplectic-and-contact-topology.html) | 6 |
| [The Graded Action on a Module over a Clifford Algebra](../articles_maths/the-graded-action-on-a-module-over-a-clifford-algebra.html) | 4 |
| [Differential Forms and Stokes' Theorem](../articles_maths/differential-forms-and-stokes-theorem.html) | 3 |
| [The Adjoint of the Clifford Multiplication](../articles_maths/the-adjoint-of-the-clifford-multiplication.html) | 3 |
| [The Clifford Multiplication Operator](../articles_maths/the-clifford-multiplication-operator.html) | 3 |
| [The Kähler Form Operator](../articles_maths/the-kahler-form-operator.html) | 3 |
| [G2 and Spin(7) Manifolds](../articles_maths/g2-and-spin7-manifolds.html) | 2 |
| [List of Symplectic Geometries](../articles_maths/list-of-symplectic-geometries.html) | 2 |
| [Peirce Carriers and Inner Conjugation](../articles_maths/peirce-carriers-and-inner-conjugation.html) | 2 |
| [The Symplectic Form and the Biquaternion Norm Cone](../articles_physics/the-symplectic-form-and-the-biquaternion-norm-cone.html) | 2 |
| [Fibre Bundles, Connections and Curvature](../articles_maths/fibre-bundles-connections-and-curvature.html) | 1 |
| [Hermitian Metrics and the Codifferential](../articles_maths/hermitian-metrics-and-the-codifferential.html) | 1 |
| [Hyperkähler Geometry](../articles_maths/hyperkahler-geometry.html) | 1 |
| [List of Clifford Algebras and Spin Groups](../articles_maths/list-of-clifford-algebras-and-spin-groups.html) | 1 |
| [Spin Geometry](../articles_maths/spin-geometry.html) | 1 |
| [The Dual Operator](../articles_maths/the-dual-operator.html) | 1 |
| [The Graded Adjoint Action on a Module over a Symmetry Group](../articles_maths/the-graded-adjoint-action-on-a-module-over-a-symmetry-group.html) | 1 |
| [The Signature Operator](../articles_maths/the-signature-operator.html) | 1 |

### The Clifford comparison — 167 occurrences in 9 articles

The Clifford comparison is the $\mathbb{R}$-linear map $\iota_{\mathrm{Cl}}:\mathbb{B}\to\mathrm{Cl}^+_{1,3}$. In cells, $\iota_{\mathrm{Cl}}(e_\mu)=T_{\mu t}$ and $\iota_{\mathrm{Cl}}(i)=T_{tz}$. Equivalently, $\iota_{\mathrm{Cl}}(\vec e_x)=\gamma_2\gamma_3$, $\iota_{\mathrm{Cl}}(\vec e_y)=\gamma_3\gamma_1$, $\iota_{\mathrm{Cl}}(\vec e_z)=\gamma_1\gamma_2$, and $\iota_{\mathrm{Cl}}(i)=-\gamma_0\gamma_1\gamma_2\gamma_3$. The image is the real span of the eight cells $T_{\mu t}$ and $T_{\mu z}$, of real dimension 8, and it satisfies $\iota_{\mathrm{Cl}}(i\tilde Q)=T_{tz}\iota_{\mathrm{Cl}}(\tilde Q)$.

The map is $\mathbb{R}$-linear and not $\mathbb{C}$-linear. A common summary writes its target as the even subalgebra of $M_4(\mathbb{C})$. That is the complexification of the even Clifford algebra, not the image: the image is the even subalgebra of $\mathrm{Cl}_{1,3}$, of real dimension 8, while the even subalgebra of $M_4(\mathbb{C})$ has complex dimension 8, hence real dimension 16. The distinction matters because the map does not commute with multiplication by the adjoined $i$; it sends $i$ to $T_{tz}$, which is not $i$ times a real cell.

The exact token $\iota_{\mathrm{Cl}}$ occurs 166 times in 9 articles. The remaining occurrence is the bare $\iota$ in the Dirac article, where the complexified extension is intended.

| Article | Occurrences |
|---|---:|
| [The Reflection and the Rotation in Biquaternionic Form](../articles_physics/the-reflection-and-the-rotation-in-biquaternionic-form.html) | 37 |
| [Conventions of the Matrix Models (physics)](../articles_physics/conventions-of-the-matrix-models.html) | 33 |
| [The Anomalous Magnetic Moment in Biquaternionic Form](../articles_physics/the-anomalous-magnetic-moment-in-biquaternionic-form.html) | 31 |
| [The Rarita–Schwinger Equation: Spin 3/2 in Biquaternionic Form](../articles_physics/the-rarita-schwinger-equation-spin-3-2-in-biquaternionic-form.html) | 20 |
| [Curved Spacetime and the Biquaternion Framework](../articles_physics/curved-spacetime-and-the-biquaternion-framework.html) | 16 |
| [Conventions of the Matrix Models (maths)](../articles_maths/conventions-of-the-matrix-models.html) | 15 |
| [The Dirac Path Integral in Biquaternionic Form](../articles_physics/the-dirac-path-integral-in-biquaternionic-form.html) | 7 |
| [The Foldy–Wouthuysen Transformation in Biquaternionic Form](../articles_physics/the-foldy-wouthuysen-transformation-in-biquaternionic-form.html) | 6 |
| [The Dirac Equation in Biquaternionic Form](../articles_physics/the-dirac-equation-in-biquaternionic-form.html) | 2 |

### The canonical embedding — 666 occurrences in 76 articles

This is one role with four constructions. In every case $\iota$ is a canonical map into a larger object: a completion, a free or universal algebra, a coproduct, a dual, or a chosen matrix representation. The letter never says which construction is meant, and the target is often the only clue.

The four kinds are separated below because they fail differently. A completion can be replaced by an inclusion only when the source is already complete; a universal map is fixed by a property; a duality evaluation is not an inclusion at all; a matrix representation depends on a choice of basis.

### Completion and dense image — 219 occurrences in 19 articles

Here $\iota:X\to\widehat X$ has dense image, and $\ker\iota$ measures the failure of the source to be separated. In the involutive setting the completion is compatible with the involution: $\widehat\sigma\circ\iota=\iota\circ\sigma$. The same letter is used for the map into a completion of a ring, a field, a module, or a uniform space.


| Article | Occurrences |
|---|---:|
| [The Involution and the Completion of a Ring](../articles_maths/the-involution-and-the-completion-of-a-ring.html) | 31 |
| [The Completion Operator](../articles_maths/the-completion-operator.html) | 27 |
| [Involutive Topological Rings and Fields](../articles_maths/involutive-topological-rings-and-fields.html) | 21 |
| [The Completion of a Sesqualgebra](../articles_maths/the-completion-of-a-sesqualgebra.html) | 21 |
| [Involutive Topological Linear Spaces](../articles_maths/involutive-topological-linear-spaces.html) | 19 |
| [Metric, Uniform and Complete Spaces](../articles_maths/metric-uniform-and-complete-spaces.html) | 19 |
| [The Completion of a Sesqualgebra with a Form](../articles_maths/the-completion-of-a-sesqualgebra-with-a-form.html) | 17 |
| [Involutive Topological Algebras](../articles_maths/involutive-topological-algebras.html) | 15 |
| [The Completion of a Hilbert Algebra](../articles_maths/the-completion-of-a-hilbert-algebra.html) | 14 |
| [Topological Rings and Fields](../articles_maths/topological-rings-and-fields.html) | 7 |
| [Involutive Banach Spaces](../articles_maths/involutive-banach-spaces.html) | 5 |
| [The Residue Operator of a Valued Field](../articles_maths/the-residue-operator-of-a-valued-field.html) | 5 |
| [The Valuation Operator](../articles_maths/the-valuation-operator.html) | 4 |
| [Topological Modules and Vector Spaces](../articles_maths/topological-modules-and-vector-spaces.html) | 4 |
| [Localization and Completion of Modules](../articles_maths/localization-and-completion-of-modules.html) | 3 |
| [Involutions of a Non-Archimedean Field](../articles_maths/involutions-of-a-non-archimedean-field.html) | 2 |
| [Involutive Valued Fields](../articles_maths/involutive-valued-fields.html) | 2 |
| [The Graded Action on a Module over a Topological Ring](../articles_maths/the-graded-action-on-a-module-over-a-topological-ring.html) | 2 |
| [List of Metric and Uniform Spaces](../articles_maths/list-of-metric-and-uniform-spaces.html) | 1 |

### Universal maps and coproduct injections — 323 occurrences in 42 articles

Here $\iota$ is fixed by a universal property: $\iota:V\to\mathrm{Cl}(V)$, $\iota:X\to F(X)$ into the free algebra, $\iota:\mathfrak g\to U(\mathfrak g)$ into the enveloping algebra, $\iota_A:A\to A\otimes B$, $\iota_i:M_i\to\bigoplus_i M_i$, the corner embeddings $\iota_k:M_k\to M_6(\mathbb{C})$, the structure maps $R\to S^{-1}R$ and $A\to M(A)$, and $\mathbb{N}\to\mathbb{Z}$.

The coproduct injections and the tensor-product maps are the most frequent. They are canonical, but they are not the same map, and the subscript is the only thing that distinguishes them.

| Article | Occurrences |
|---|---:|
| [Multipliers of a Banach Algebra](../articles_maths/multipliers-of-a-banach-algebra.html) | 31 |
| [Localization and the Fraction Field](../articles_maths/localization-and-the-fraction-field.html) | 28 |
| [Opposite Algebras and Anti-Isomorphisms](../articles_maths/opposite-algebras-and-anti-isomorphisms.html) | 22 |
| [The Integers ($\mathbb{Z}$)](../articles_maths/the-integers.html) | 22 |
| [Universal Enveloping Algebras](../articles_maths/universal-enveloping-algebras.html) | 15 |
| [Tensor Products of Sesqualgebras](../articles_maths/tensor-products-of-sesqualgebras.html) | 14 |
| [The Order Unit as an Operator](../articles_maths/the-order-unit-as-an-operator.html) | 14 |
| [The Symmetric Algebra of a Module with an Involution](../articles_maths/the-symmetric-algebra-of-a-module-with-an-involution.html) | 14 |
| [Direct Sums, Free Modules and Rank](../articles_maths/direct-sums-free-modules-and-rank.html) | 11 |
| [The $M_3\oplus M_3$ and $M_2\oplus M_4$ Corners of $M_6(\mathbb{C})$](../articles_maths/the-m3-m3-and-m2-m4-corners-of-m6c.html) | 11 |
| [Topological Tensor Products of Sesqualgebras](../articles_maths/topological-tensor-products-of-sesqualgebras.html) | 11 |
| [Abelian and Grothendieck Categories](../articles_maths/abelian-and-grothendieck-categories.html) | 9 |
| [Clifford Algebras](../articles_maths/clifford-algebras.html) | 9 |
| [Tensor Powers and the Free Algebra](../articles_maths/tensor-powers-and-the-free-algebra.html) | 8 |
| [Module Categories](../articles_maths/module-categories.html) | 7 |
| [The Suspension Operator](../articles_maths/the-suspension-operator.html) | 7 |
| [Generators, Presentations and Free Products](../articles_maths/generators-presentations-and-free-products.html) | 6 |
| [The Adjoint of the Left and the Right Multiplication](../articles_maths/the-adjoint-of-the-left-and-the-right-multiplication.html) | 6 |
| [The Balanced Product over an Algebra](../articles_maths/the-balanced-product-over-an-algebra.html) | 6 |
| [The $M_2\oplus M_3$ Corner of $M_5(\mathbb{C})$](../articles_maths/the-m2-m3-corner-of-m5c.html) | 6 |
| [Commutative Algebras](../articles_maths/commutative-algebras.html) | 5 |
| [Differential Topology](../articles_maths/differential-topology.html) | 5 |
| [The Adjoint of the Left Multiplication on a Hermitian Algebra](../articles_maths/the-adjoint-of-the-left-multiplication-on-a-hermitian-algebra.html) | 5 |
| [The Involution on the Multiplication Operators](../articles_maths/the-involution-on-the-multiplication-operators.html) | 5 |
| [Hilbert and C*-Modules](../articles_maths/hilbert-and-c-star-modules.html) | 4 |
| [K-Theory of Operator Algebras](../articles_maths/k-theory-of-operator-algebras.html) | 4 |
| [Semiprime Rings](../articles_maths/semiprime-rings.html) | 4 |
| [The $M_2$ Corner of $M_3(\mathbb{C})$](../articles_maths/the-m2-corner-of-m3c.html) | 4 |
| [Universal Properties and Categories](../articles_maths/universal-properties-and-categories.html) | 4 |
| [Continuous Maps as Operators](../articles_maths/continuous-maps-as-operators.html) | 3 |
| [The Left and Right Multiplication Operators on a Banach Algebra](../articles_maths/the-left-and-right-multiplication-operators-on-a-banach-algebra.html) | 3 |
| [Degree Theory and the Brouwer Fixed Point Theorem](../articles_maths/degree-theory-and-the-brouwer-fixed-point-theorem.html) | 2 |
| [Grassmannians and Stiefel Manifolds](../articles_maths/grassmannians-and-stiefel-manifolds.html) | 2 |
| [Noetherian and Artinian Rings](../articles_maths/noetherian-and-artinian-rings.html) | 2 |
| [Primary Decomposition](../articles_maths/primary-decomposition.html) | 2 |
| [Smooth Manifolds and Differential Geometry](../articles_maths/smooth-manifolds-and-differential-geometry.html) | 2 |
| [The Balanced Product](../articles_maths/the-balanced-product.html) | 2 |
| [The Euclidean Topology of the Biquaternion Algebra](../articles_maths/the-euclidean-topology-of-the-biquaternion-algebra.html) | 2 |
| [The Left and the Right Regular Representation](../articles_maths/the-left-and-the-right-regular-representation.html) | 2 |
| [The Modular Structure of a Hermitian Algebra](../articles_maths/the-modular-structure-of-a-hermitian-algebra.html) | 2 |
| [Self-Adjoint Operators of a Banach Algebra](../articles_maths/self-adjoint-operators-of-a-banach-algebra.html) | 1 |
| [The Tomita Operator and the J-Modular Pair for the Biquaternion Algebra](../articles_maths/the-tomita-operator-and-the-j-modular-pair-for-the-biquaternion-algebra.html) | 1 |

### Duality — 72 occurrences in 8 articles

Here $\iota_G:G\to G^{\vee\vee}$ is the evaluation into the bidual, and $\iota_E:E\to E''$ is the same map for a topological vector space. It is not an inclusion in general: it is injective exactly when the space is semireflexive.


| Article | Occurrences |
|---|---:|
| [Pontryagin Duality](../articles_maths/pontryagin-duality.html) | 19 |
| [The Dual Operator](../articles_maths/the-dual-operator.html) | 18 |
| [The Dual Pairing and the Adjoint](../articles_maths/the-dual-pairing-and-the-adjoint.html) | 14 |
| [Duality Theory](../articles_maths/duality-theory.html) | 7 |
| [Profinite Groups and the Krull Topology](../articles_maths/profinite-groups-and-the-krull-topology.html) | 5 |
| [The Dual Operator and the Weak Topology](../articles_maths/the-dual-operator-and-the-weak-topology.html) | 4 |
| [Abelian Topological Groups](../articles_maths/abelian-topological-groups.html) | 3 |
| [Harmonic Analysis on Groups](../articles_maths/harmonic-analysis-on-groups.html) | 2 |

### Matrix representations — 52 occurrences in 7 articles

Here $\iota$ is a chosen representation: $\mathbb{H}\to M_2(\mathbb{C})$, $\mathbb{B}\to\mathbb{R}^8$ in idempotent coordinates, or the map that sends an element to its matrix of Peirce components. It is canonical only after the basis is fixed, and the same letter is used for the coordinates themselves.


| Article | Occurrences |
|---|---:|
| [Quaternion Other Algebraic Element Representations](../articles_maths/quaternion-other-algebraic-element-representations.html) | 16 |
| [Modulus–Unit Polar Decomposition of Quaternions](../articles_maths/modulus-unit-polar-decomposition-of-quaternions.html) | 12 |
| [Reduced Biquaternion Versors and the Orthogonal Group](../articles_maths/reduced-biquaternion-other-algebraic-element-representations.html) | 9 |
| [Determinants in Jordan Matrix Algebras](../articles_maths/determinants-in-jordan-matrix-algebras.html) | 5 |
| [Exponential Polar Decomposition of Quaternions](../articles_maths/exponential-polar-decomposition-of-quaternions.html) | 5 |
| [Rational-Chart Polar Decomposition of Quaternions](../articles_maths/rational-chart-polar-decomposition-of-quaternions.html) | 3 |
| [Comparison of Element Representations and Matrix Models](../articles_maths/comparison-of-element-representations-and-matrix-models.html) | 2 |

### The fundamental class — 27 occurrences in 2 articles

The fundamental class is $\iota_n\in H^n(K(\pi,n);\pi)$, the class that corresponds to the identity of $\pi$ under the Hurewicz isomorphism. The letter is standard in algebraic topology, and the subscript is the degree. The same form $\iota_n$ also occurs three times in the statistics article as a quaternion involution with axis $n$; that is a genuine collision, but it is local and easy to qualify.

| Article | Occurrences |
|---|---:|
| [Classifying Spaces and Cohomology Operations](../articles_maths/classifying-spaces-and-cohomology-operations.html) | 25 |
| [The Leray–Serre Spectral Sequence](../articles_maths/the-leray-serre-spectral-sequence.html) | 2 |

### The involution of a space — 69 occurrences in 3 articles

The involution of a space is a map $\iota:X\to X$ with $\iota^2=\mathrm{id}$. On a manifold it is the geodesic involution $\iota(v)=-v$ on the tangent bundle, or an isometry $\iota\in\Gamma$ acting on $M$. On a Hermitian manifold it is the real structure that defines the indefinite metric.

The letter is the same as the group inversion because both are order-two maps. The difference is the category: one is a map of a group, the other a map of a space.

| Article | Occurrences |
|---|---:|
| [The Signature Operator and the Involution](../articles_maths/the-signature-operator-and-the-involution.html) | 43 |
| [Hermitian Manifolds and the Geodesic Involution](../articles_maths/hermitian-manifolds-and-the-geodesic-involution.html) | 24 |
| [Hermitian Pairings and the Index](../articles_maths/hermitian-pairings-and-the-index.html) | 2 |

### The angular velocity — 85 occurrences in 1 article

In the moving-frame article, $\iota$ is the $\mathbb{B}$-valued position of the frame, and $\iota_1,\iota_2,\iota_3$ are the components of its angular velocity: $d\iota=\iota_1\vec e_x+\iota_2\vec e_y+\iota_3\vec e_z$. Each $\iota_k$ is a real one-form, not an involution and not a basis element.

The same article writes $\iota_F$ for the Frenet frame, which is the same construction restricted to a curve. The subscript does the work that the letter cannot.

| Article | Occurrences |
|---|---:|
| [Curves and Surfaces in the Biquaternion Moving Frame](../articles_maths/curves-and-surfaces-in-the-biquaternion-moving-frame.html) | 85 |

### The moving-frame map — 28 occurrences in 1 article

The moving-frame map $\iota$ is the $\mathbb{B}$-valued position of the frame, with $d\iota=2r^\dagger dr$. The differential is the connection one-form; $\iota$ itself is not a curve, and $r$ is the rotor. The article also writes $\iota_F$ for the Frenet frame.

The map is confined to one article and has 28 occurrences: 24 bare and 4 with the subscript $F$. The same article uses the bare letter for a second object, treated next.

| Article | Occurrences |
|---|---:|
| [Curves and Surfaces in the Biquaternion Moving Frame](../articles_maths/curves-and-surfaces-in-the-biquaternion-moving-frame.html) | 28 |

### The grade-two element — 6 occurrences in 1 article

The same article uses $\iota,\iota'\in\mathbb{G}_2$ for grade-two elements, in the identity $\iota\wedge\iota'=V(\iota)\times V(\iota')$. Here $\iota$ is a vector of the Lie algebra $\mathfrak{so}(3)$, not the frame map. The two uses are a few paragraphs apart, and the only signal is the type: one is a map into $\mathbb{B}$, the other an element of $\mathbb{G}_2$.

This is one of the smallest objects in the corpus and the clearest example of a collision inside a single article. A scope declaration at the top of the article would not separate them, because both uses are in the same scope.

| Article | Occurrences |
|---|---:|
| [Curves and Surfaces in the Biquaternion Moving Frame](../articles_maths/curves-and-surfaces-in-the-biquaternion-moving-frame.html) | 6 |

### The Newman-Penrose spinor — 26 occurrences in 1 article

In the Newman–Penrose formalism, $o$ and $\iota$ are the two basis spinors: $o=(1,0)^T$, $\iota=(0,1)^T$, with $\varepsilon(o,\iota)=1$. The components are $\iota_1$ and $\iota_2$, and the conjugate is $\iota^A$. This is standard notation in general relativity, and it is confined to one article.


| Article | Occurrences |
|---|---:|
| [The Newman–Penrose Formalism in Biquaternionic Form](../articles_physics/the-newman-penrose-formalism-in-biquaternionic-form.html) | 26 |

### The identity map — 18 occurrences in 1 article

In the quantum-group article, $\iota$ is the identity of the multiplier algebra, characterized by $(\iota\otimes\varphi)\Delta(a)=\varphi(a)1$ and $(\varphi\otimes\iota)\Delta(a)=\varphi(a)1$. It is not a map between two different objects, and the letter is not the identity map of a set.


| Article | Occurrences |
|---|---:|
| [Locally Compact Quantum Groups](../articles_maths/locally-compact-quantum-groups.html) | 18 |

### The base type — 5 occurrences in 1 article

In the type-theory article, $\iota$ is a base type in the Church encoding of the natural numbers: $(\iota\to\iota)\to\iota\to\iota$. It is a variable, not an operator.


| Article | Occurrences |
|---|---:|
| [Proof Theory and Type Theory](../articles_maths/proof-theory-and-type-theory.html) | 5 |

### The algebra element — 2 occurrences in 1 article

In the spectral-regularity article, $\iota=1\otimes i$ is the adjoined imaginary of the complexified algebra, and $e_\pm=\frac12(1\mp i\iota)$ are the idempotents it defines. The letter names an element, not a map.


| Article | Occurrences |
|---|---:|
| [Spectral Regularity and Degeneracy in the Complex Algebra](../articles_maths/spectral-regularity-and-degeneracy-in-the-complex-algebra.html) | 2 |

### The index label — 1 occurrence in 1 article

In the table of index letters, ${}_{\iota}$ is a label in a list. It names no mathematical object. It is included for completeness because a search for the letter finds it.


| Article | Occurrences |
|---|---:|
| [Conventions of the Indices, the Notation and the Corpus](../articles_maths/conventions-of-the-indices-the-notation-and-the-corpus.html) | 1 |

## The Collisions

A collision is a written form that names more than one reading. The table gives every form that does so, with the readings and their counts. Forms not listed are stable: $\iota_{\mathrm{Cl}}$ (166 exact), $\iota_X$ (71 exact), the $\iota_\nu$ family (81), and the long qualified subscripts.

| Form | Occurrences | Readings |
|---|---:|---|
| $\iota$ (bare) | 888 | inversion 279; completion 182; universal map 176; anti-automorphism 86; matrix representation 50; space involution 38; interior product 19; moving-frame map 13; NP spinor 13; identity 9; duality 8; grade-two element 5; type 5; algebra element 2; index label 1; quaternion involution 1; Clifford comparison 1 |
| $\iota_u$ | 81 | inner automorphism 66; order-unit embedding 14; interior product 1 |
| $\iota_i$ | 10 | coproduct inclusion 7; octonion unit 3 |
| $\iota_j$ | 61 | quaternion involution 53; coproduct inclusion 5; angular velocity 3 |
| $\iota_k$ | 56 | quaternion involution 43; corner embedding 13 |
| $\iota_1$ | 59 | angular velocity 29; quaternion involution 16; fundamental class 7; coproduct inclusion 3; octonion unit 2; inner automorphism 1; NP spinor 1 |
| $\iota_2$ | 54 | angular velocity 31; quaternion involution 15; fundamental class 3; coproduct inclusion 3; octonion unit 1; NP spinor 1 |
| $\iota_3$ | 41 | angular velocity 22; quaternion involution 15; fundamental class 3; octonion unit 1 |
| $\iota_n$ | 17 | fundamental class 14; quaternion involution 3 |

These 1,250 occurrences — the bare letter and the seven forms from $\iota_u$ to $\iota_3$ — are more than half of the corpus. A reader who meets one of them cannot resolve it from the letter alone.

### The bare letter — 888 occurrences

The bare letter is the worst case because it carries no information at all. Its 888 occurrences cover thirteen of the seventeen objects, plus the one label. The four largest are the inversion (279), the completion (182), the universal map (176), and the anti-automorphism (86). The matrix representation (50) and the space involution (38) follow; the rest are small but not negligible.

A local declaration can fix a single article. Nothing can fix a formula copied from one article to another without its declaration. The corpus already contains such a copy: the Dirac article uses the bare $\iota$ for the complexified Clifford comparison, while the same bare letter in the neighbouring articles is the inversion or the embedding.

### The subscript $u$ — 81 occurrences

$\iota_u$ is the inner automorphism in 66 occurrences and the order-unit embedding $\iota_u:R\to E$ in 14. The remaining occurrence is an interior product $\iota_u\varphi$ in the $G_2$ article. Three objects, one form.

The inner automorphism and the order-unit map are both canonical, and both are written with the element that defines them. The reader has to know whether $u$ is a unit or an order unit before the formula makes sense.

### The subscripts $i$, $j$, $k$

$\iota_i$ is the coproduct inclusion in 7 occurrences and the octonion unit in 3. The octonion use is confined to one article, but the inclusion use is spread over four.

$\iota_j$ is the quaternion involution in 53 occurrences, the coproduct inclusion in 5, and the angular velocity in 3. The angular velocity is the only one where $\iota_j$ is a one-form, so the type distinguishes it after the fact, not at sight.

$\iota_k$ is the quaternion involution in 43 occurrences and the corner embedding in 13. The first is a map $\mathbb{H}\to\mathbb{H}$; the second is a map $M_k\to M_6(\mathbb{C})$. The target distinguishes them only if the reader already knows the article.

### The numerals $1$, $2$, $3$ — 154 occurrences

The numerals are the densest collision. $\iota_1$ alone names seven objects: the angular velocity component (29), the quaternion involution (16), the fundamental class (7), the coproduct inclusion (3), the octonion unit (2), the inner automorphism at the identity (1), and the NP spinor component (1). $\iota_2$ names six, and $\iota_3$ names four. Together they occur 154 times.

The reason is structural. Every construction that needs a countable family uses the same numerals: a basis, a coordinate axis, a degree, a direct summand. The letter does not say which family is meant, and the numeral is the only part that varies.

### The forms that do not collide

$\iota_{\mathrm{Cl}}$ is unique to the Clifford comparison, except for the one bare occurrence in the Dirac article. $\iota_X$ is unique to the interior product; its variants change the vector, not the object. The $\iota_\nu$ family is unique to the quaternion involution, even when the axis is composite. These are the forms a repair should keep.

$\iota_n$ would be stable if the statistics article did not use the same form for an involution with axis $n$. The three occurrences are easy to qualify as $\iota_{n,\mathrm{stat}}$ or by renaming the axis.

### The one undefined occurrence

The Dirac article writes $\iota(\tilde\Xi_{\mathrm{ad}})$ without defining $\iota$. The surrounding sentence says that both $\iota(\tilde\Xi_{\mathrm{ad}})=+i_{\mathrm{Cl}}$ and the negative sign are admissible. The map is the complexified extension of $\iota_{\mathrm{Cl}}$, but the letter does not say so.

This occurrence is undefined in its own article. It is also the clearest evidence that the letter is being used as inherited notation: the author expects the reader to carry $\iota_{\mathrm{Cl}}$ from another article, and the bare letter is the result.

## What a Repair Would Cost

A global replacement is impossible. Replacing every $\iota$ by one name would relabel the inversion, the embedding, the anti-automorphism, the interior product, and the rest with the same wrong name. The replacement has to be chosen per occurrence, and 888 occurrences have no subscript to guide the choice.

The mechanical cost is 2,336 edits in 196 files. The intellectual cost is larger: 1,250 occurrences are in a form that names more than one object, and four articles mix objects under the same letter — *Curves and Surfaces in the Biquaternion Moving Frame* (moving-frame map, angular velocity, and grade-two element), *The Dual Operator* (interior product and duality), *The Generalised Hamilton–Rodrigues Calculus* (inner automorphism and quaternion involution), and *Quaternion Involutions and Projections* (inner automorphism and quaternion involution).

A rename of the stable forms would cost 167 edits for $\iota_{\mathrm{Cl}}$ and 274 for the interior product, and would buy nothing. The repair should leave them alone.

The minimal repair is a scope declaration in every article that uses the bare letter, plus a qualified subscript for the ambiguous forms. That is a change of notation, not a change of mathematics, and it can be done article by article.

## A Naming Proposal

The proposal is a direction, not an edit. It keeps the standard forms and qualifies the ambiguous ones. No new bare letter is introduced; the corpus is already dense with single-letter operators.

| Object | Current | Proposal | Note |
|---|---|---|---|
| Group inversion | $\iota$ | $\operatorname{inv}$ or a declared local $\iota$ | the composite $\sigma\iota$ becomes $\sigma\circ\operatorname{inv}$ |
| Anti-automorphism | $\iota$ | $\iota_{\mathrm{anti}}$ | the article must say which algebra |
| Inner automorphism | $\iota_u$ | $\operatorname{Ad}_u$ | already used in the corpus |
| Quaternion involution | $\iota_\nu$ | keep | the subscript names the axis |
| Octonion units | $\iota_i$ | $e_i$ or a declared local $\iota_i$ | the only article where the letter is a basis |
| Interior product | $\iota_X$ | keep | standard |
| Clifford comparison | $\iota_{\mathrm{Cl}}$ | keep | the one globally fixed form |
| Completion | $\iota$ | $\iota_{\mathrm{comp}}$ | dense image |
| Universal map | $\iota$ | $\iota_{\mathrm{can}}$ | the property fixes it |
| Coproduct inclusion | $\iota_i$ | keep with the index | the index names the summand |
| Duality | $\iota_G$ | $\iota_{\mathrm{ev}}$ | evaluation, not inclusion |
| Matrix representation | $\iota$ | $\iota_{\mathrm{mat}}$ | depends on the basis |
| Fundamental class | $\iota_n$ | keep | standard in topology |
| Space involution | $\iota$ | $\iota_M$ with the space named | or a declared local letter |
| Angular velocity | $\iota_k$ | keep local, declared | the type is a one-form |
| Moving-frame map | $\iota$ | $\iota_{\mathrm{fr}}$ | $\gamma$ and $r$ are taken in the same article |
| NP spinor | $\iota$ | keep | standard in general relativity |
| Identity map | $\iota$ | $\mathrm{id}$ | no ambiguity |
| Base type | $\iota$ | keep local | a type variable |
| Algebra element | $\iota$ | $\iota_{\mathbb C}$ | the adjoined imaginary |
| Index label | ${}_{\iota}$ | none | a label, not an object |

The table is deliberately conservative. $\operatorname{Ad}_u$ is the only borrowed notation that is already standard in the corpus. The qualified subscripts use words that the articles already use, so a reader can resolve them without a glossary.

## Summary

$\iota$ is not one symbol with one meaning. It is 115 spellings and seventeen objects, plus one index label, and 1,250 occurrences are written in a form that names more than one reading. The Clifford comparison and the interior product are stable; the octonion units are stable only inside their article. The damage is in the bare letter and the small numerals.

The exact figures are: 2,336 occurrences in 196 articles, in 115 spellings. The objects are: 666 canonical embeddings; 348 quaternion involutions; 335 inversions; 274 interior products; 169 inner automorphisms; 167 Clifford comparisons; 98 anti-automorphisms; 85 angular velocities; 69 space involutions; 28 moving-frame maps; 27 fundamental classes; 26 NP spinors; 18 identity maps; 12 octonion units; 6 grade-two elements; 5 type variables; 2 algebra elements. One further occurrence is the index label ${}_{\iota}$, which names no object. Of the occurrences, 888 are the bare letter and 1,250 are in a colliding form.

## Summary of Notation

| Form | Meaning in this article |
|---|---|
| $\iota$ | the letter under study, quoted rather than used |
| $\iota_{\mathrm{Cl}}$ | the Clifford comparison, $\mathbb{B}\to\mathrm{Cl}^+_{1,3}$ |
| $\iota_X$ | the interior product |
| $\iota_u$ | the inner automorphism, or the order-unit embedding |
| $\iota_i$ | an octonion unit, or a coproduct inclusion |
| $\iota_1,\iota_2,\iota_3$ | angular velocity, quaternion involution, fundamental class, or basis index |
| $\sigma\iota$ | the composite of an involution with the inversion |
| $\iota_n$ | the fundamental class of $K(\pi,n)$ |

## Further Reading

The conventions articles set the surrounding notation:

- [Conventions of the Indices, the Notation and the Corpus](../articles_maths/conventions-of-the-indices-the-notation-and-the-corpus.html) defines the index letters, including ${}_{\iota}$.
- [Conventions of the Operators and the Differential Calculus](../articles_maths/conventions-of-the-operators-and-the-differential-calculus.html) fixes the operator conventions.
- [Conventions of the Matrix Models](../articles_maths/conventions-of-the-matrix-models.html) and its [physics counterpart](../articles_physics/conventions-of-the-matrix-models.html) define $\iota_{\mathrm{Cl}}$ and its cells.

The standard forms have their articles: [The Exterior Derivative](../articles_maths/the-exterior-derivative.html) for the interior product, [Special and Exceptional Jordan Algebras](../articles_maths/special-and-exceptional-jordan-algebras.html) for the octonion units, and [Involutive Groups](../articles_maths/involutive-groups.html) for the inversion.

The four articles that mix objects under one letter are [Curves and Surfaces in the Biquaternion Moving Frame](../articles_maths/curves-and-surfaces-in-the-biquaternion-moving-frame.html), [The Dual Operator](../articles_maths/the-dual-operator.html), [The Generalised Hamilton–Rodrigues Calculus](../articles_maths/the-generalised-hamilton-rodrigues-calculus.html), and [Quaternion Involutions and Projections](../articles_maths/quaternion-involutions-and-projections.html).

[The Upper Indexes Problem](the-upper-indexes-problem.html) applies the same method to the index conventions and is the model for this inventory.
