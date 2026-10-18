# __The Monoid of Acting Maps: the Process Is the Multiplication, the State Is the Idempotent__

## Introduction

Two articles of the corpus describe an element of the biquaternion algebra as an operator. *The 2×2 Matrix Operator Representation $M_2(\mathbb{C})\otimes M_2(\mathbb{C})$ of Biquaternions* writes the sandwich $\operatorname{H}_{\tilde{Q}_1}(\tilde{Q}_2) = \tilde{Q}_1\tilde{Q}_2\tilde{Q}_1^{*}$ as the congruence $X\mapsto M X M^{\dagger}$ on the matrix image, and *The 4×4 Matrix Operator Representation $M_4(\mathbb{C})$ of Biquaternions* writes the same sandwich as a product of the two regular maps, $\operatorname{H}_{\tilde{Q}_1} = L_{\tilde{Q}_1}\circ R_{\tilde{Q}_1^{*}}$. Both are statements about a matrix that represents the element.

This article records the abstract statement that the two matrix articles realize. An element **is** the map "multiply by it": the left multiplication $L_{\tilde{Q}_1}:\tilde{Q}_2\mapsto\tilde{Q}_1\tilde{Q}_2$ and the right multiplication $R_{\tilde{Q}_1}:\tilde{Q}_2\mapsto\tilde{Q}_2\tilde{Q}_1$ are two $\mathbb{C}$-linear maps of the algebra attached to one element, and the composition of these maps makes the set of acting maps a **monoid**. The process is the map and not the element; the elements compose well because the maps compose, and the order of the composition is the order of the operations. The sandwich of the two operator articles is the composition of a left action with a right action, which is why one article sees a congruence and the other a product of two regular matrices.

The second half turns to the other half of the dictionary. The **pure states** of the framework are the Hermitian idempotents, not the maps: a Hermitian idempotent is an idempotent fixed by the star; the Hermitian idempotents that carry the states lie in the informational sector, the material sector has none, and the multiplication operator an idempotent generates is a **non-invertible** map. So the dictionary of the article is one line. The **process** is the map side, where the reversible processes are the units off the light cone; the **state** is the Hermitian idempotent side, and the rank-one Hermitian idempotents are null, so they lie **on** the light cone. The cone is therefore not a border between two disjoint halves: it is where the non-invertible maps are and where the states sit, while a unit is an element off the cone.

## The Two One-Sided Actions

For an element $\tilde{Q}_3$ of the algebra, the **left multiplication** and the **right multiplication** are the maps

$$
L_{\tilde{Q}_3} : \tilde{Q}_2 \mapsto \tilde{Q}_3\tilde{Q}_2, \qquad\qquad R_{\tilde{Q}_3} : \tilde{Q}_2 \mapsto \tilde{Q}_2\tilde{Q}_3.
$$

Both are $\mathbb{C}$-linear endomorphisms of $\mathbb{B}$, and both are determined by the element: $L_{\tilde{Q}_3}(e_t) = \tilde{Q}_3$ and $R_{\tilde{Q}_3}(e_t) = \tilde{Q}_3$. Their **composition rules** are the associativity of the product read on the maps,

$$
L_{\tilde{Q}_3}\circ L_{\tilde{Q}_1} = L_{\tilde{Q}_3\tilde{Q}_1}, \qquad\qquad R_{\tilde{Q}_3}\circ R_{\tilde{Q}_1} = R_{\tilde{Q}_1\tilde{Q}_3},
$$

and the two families **commute** with one another,

$$
L_{\tilde{Q}_3}\circ R_{\tilde{Q}_1} = R_{\tilde{Q}_1}\circ L_{\tilde{Q}_3},
$$

for every pair, because $\tilde{Q}_3(\tilde{Q}_2\tilde{Q}_1) = (\tilde{Q}_3\tilde{Q}_2)\tilde{Q}_1$ is the same associativity. The first of the two rules is the one the article turns on: **the left multiplications compose into the left multiplication of the product**, so the correspondence between elements and left multiplications respects the multiplication, whereas the right multiplications compose in the reverse order, since the product is not commutative.

### The Regular Representation

The rule $L_{\tilde{Q}_3}\circ L_{\tilde{Q}_1} = L_{\tilde{Q}_3\tilde{Q}_1}$ has a name and a consequence. The map

$$
\tilde{Q}_1\;\longmapsto\; L_{\tilde{Q}_1}
$$

is an **injective algebra homomorphism** from $\mathbb{B}$ into the endomorphisms of $\mathbb{B}$: it is linear, it respects the product by the rule, it carries $e_t$ to the identity map, and it is injective because $L_{\tilde{Q}_1}(e_t) = \tilde{Q}_1$ recovers the element from the map. This is the **left regular representation** of the algebra, and it is the abstract content of the two matrix operator articles: what those articles tabulate in matrices is the image of this homomorphism, $L_{\tilde{Q}_1}$ read in the coefficient basis.

## The Monoid of Acting Maps

The image of the regular representation is the set of left multiplications,

$$
\mathcal{L} = \{\,L_{\tilde{Q}_1} \;:\; \tilde{Q}_1\in\mathbb{B}\,\},
$$

and its structure is fixed by the composition rule. Composition of maps is associative always, so $\mathcal{L}$ is **associative**; the identity element is the left multiplication by the algebra's unit, $L_{e_t} = \mathrm{id}$; and $\mathcal{L}$ is closed under composition by the rule. Therefore

$$
(\mathcal{L},\,\circ,\;L_{e_t})
$$

is a **monoid**: a set with an associative product and an identity. It is not a group, and the reason is the algebra's zero divisors. The element $L_{\tilde{Q}_1}$ is invertible **iff** $\tilde{Q}_1$ is a unit, that is iff $\langle\tilde{Q}_1\rangle_{\natural}\neq0$, in which case $L_{\tilde{Q}_1}^{-1} = L_{\tilde{Q}_1^{-1}}$ with $\tilde{Q}_1^{-1} = \tilde{Q}_1^{\natural}/\langle\tilde{Q}_1\rangle_{\natural}$; if $\langle\tilde{Q}_1\rangle_{\natural} = 0$ the element is a zero divisor and $L_{\tilde{Q}_1}$ is not invertible. So the group of units of the monoid is the image of the group of invertible elements, and **the zero divisors are the non-invertible maps**.

Two features of the monoid are read physically and are stated here before the interpretation. The first is that the monoid is **oriented**. Since the product does not commute, $L_{\tilde{Q}_3\tilde{Q}_1}\neq L_{\tilde{Q}_1\tilde{Q}_3}$ in general, so the composition of the maps remembers the order of the operations; the element is an **ordered** operation and not a magnitude, and the same two operations composed in the two orders give two different maps. This is the map-level form of the corpus's statement that the material composition is oriented and cannot measure. The second is that the monoid has a **zero**: the zero element of the algebra gives the zero map, $L_0 = 0$, and it is absorbing, $L_{\tilde{Q}_1}\circ L_0 = L_0$. A monoid with a zero and with non-invertible elements is exactly the shape of a set of **processes** that can be composed and that can fail to be reversed, and this is the shape the interpretation uses.

## Units and Zero Divisors: the Boundary of the Monoid

The invertibility of the maps cuts the algebra into two classes, and the cut is the light cone. An element is a **unit** iff $\langle\tilde{Q}_1\rangle_{\natural}\neq0$, that is off the null cone; and it is a **zero divisor** iff it is null, on the cone. In the monoid this is the boundary between the invertible maps and the non-invertible ones:

$$
\underbrace{\langle\tilde{Q}_1\rangle_{\natural}\neq0}_{\text{units, invertible maps}} \qquad\big|\qquad \underbrace{\langle\tilde{Q}_1\rangle_{\natural}=0}_{\text{zero divisors, non-invertible maps}} ,
$$

and the boundary is the light cone $\langle\tilde{Q}_1\rangle_{\natural}=0$, the locus the corpus reads as the causal boundary. A process off the cone can be undone by its inverse map; a process on the cone cannot, because the map has a kernel. The article records the identification: **the group of units of the monoid is the off-cone part of the algebra, and the cone is the set of processes that cannot be reversed.**

## The Sandwich as a Composition of Two Actions

The operator of the two matrix articles is the composition of a left action with a right action. With the Hermitian conjugation ${}^{*}$,

$$
\operatorname{H}_{\tilde{Q}_1}(\tilde{Q}_2) = \tilde{Q}_1\tilde{Q}_2\tilde{Q}_1^{*} = L_{\tilde{Q}_1}\bigl(R_{\tilde{Q}_1^{*}}(\tilde{Q}_2)\bigr) = (L_{\tilde{Q}_1}\circ R_{\tilde{Q}_1^{*}})(\tilde{Q}_2),
$$

so that

$$
\operatorname{H}_{\tilde{Q}_1} = L_{\tilde{Q}_1}\circ R_{\tilde{Q}_1^{*}}.
$$

This is the abstract form of both matrix statements. Read in the coefficient basis it is the $4\times4$ regular operator, the product of the left regular matrix of $\tilde{Q}_1$ and the right regular matrix of its conjugate, $L_{\tilde{Q}_1}\circ R_{\tilde{Q}_1^{*}}$; read through the matrix image $\mathsf{M}_2$ it is the congruence $X\mapsto M X M^{\dagger}$. The two operator articles are the two matrix forms of one composition, and the composition is taken in the monoid above. The sandwich is the composite of a left multiplication (an element of $\mathcal{L}$) with a right multiplication (an element of the opposite monoid $\mathcal{R}$), so it lies in the larger monoid generated by both actions and it is generally **not** a left multiplication: $\operatorname{H}_{\tilde{Q}_1}$ equals $L_{\tilde{Q}_1\tilde{Q}_1^{*}}$ exactly when $\tilde{Q}_1$ is central, and otherwise the two differ. That is the map-level reason the sandwich is a congruence and not a similarity, and it is why the corpus reads it as a transformation rather than as a state.

## The State Side: Idempotents

The **state projectors** of the framework are the Hermitian idempotents: a Hermitian idempotent is an element $\tilde{\Pi}^2 = \tilde{\Pi} = \tilde{\Pi}^{*}$, its rank measures the mixing, and the rank-one Hermitian idempotents are the pure states. Under the regular representation an idempotent element gives an idempotent map,

$$
\tilde{\Pi}^2 = \tilde{\Pi} \quad\Longleftrightarrow\quad L_{\tilde{\Pi}}\circ L_{\tilde{\Pi}} = L_{\tilde{\Pi}},
$$

since $L_{\tilde{\Pi}}^2 = L_{\tilde{\Pi}^2}$ and the representation is injective. So the dictionary has both entries on the same footing: **an idempotent element corresponds to an idempotent map**, and the projector is the map its left multiplication generates. The corpus fixes where they live. There is no nonzero idempotent in the material sector $\mathbb{M}_-$; the **Hermitian idempotents** lie in the informational sector $\mathbb{M}_+$, while a general idempotent of the algebra need not be Hermitian and need not lie in either sector; and the **minimal** idempotents are the rank-one Hermitian idempotents, $\tilde{\Pi}\tilde{Q}_1\tilde{\Pi} = \mathrm{Tr}(\tilde{\Pi}\tilde{Q}_1)\,\tilde{\Pi} = 2\,\mathrm{Sc}(\tilde{\Pi}\tilde{Q}_1)\,\tilde{\Pi}$, whose images are the single Hermitian lines the corpus reads as pure states and as the vacua of single modes. A minimal idempotent gives a **rank-one** map, the algebraic shape of a measurement outcome, and its element is **null**, $\langle\tilde{\Pi}\rangle_{\natural} = 0$, so the states sit on the light cone.

## The Reading: the Process Is the Map, the State Is the Idempotent

The dictionary is now complete and it is read in one paragraph. An element of the algebra has two faces. Its face as a **process** is the map it generates, the left multiplication $L_{\tilde{Q}_1}$, and the processes form a monoid: they compose associatively, the order matters, the identity is the unit, and the reversible ones are the units off the light cone. Its face as a **pure state** is the Hermitian idempotent it can be, and the pure states are the rank-one Hermitian idempotents of the informational sector. The two faces are different objects of the same algebra: a **process** is a map, invertible exactly off the cone, and a **state** is a Hermitian idempotent, the minimal ones null and sitting on the cone.

Read physically, the interpretation is the framework's **process–state split** stated algebraically. A physical operation that can be composed and undone is a left multiplication of the monoid, off the cone; a measurement is a projection, an idempotent of the informational sector; and the collapse of a measurement is the passage from an invertible map to a non-invertible one, which the sandwich of the operator articles performs on the cone. The framework's own version of this passage is *Decoherence as Idempotent Projection* and the rank-one collapse read in *The 2×2 Matrix Operator Representation $M_2(\mathbb{C})\otimes M_2(\mathbb{C})$ of Biquaternions*; the map-level statement here is that the collapse is a **non-invertible element of the monoid**, and the reversible dynamics is the group of its units. The algebra supplies both, and it supplies the light cone as the boundary between the reversible and the non-reversible.

## What the Reading Does Not Claim

- The interpretation does **not** add an operator algebra structure to the states. The monoid of maps is not a $C^{*}$-algebra, the idempotents are not given a trace rule by it, and the states remain the Hermitian idempotents of the framework; the trace and the positivity are *The Biquaternioid General Plain Sesqualgebra (GPS) over $\mathbb{C}$*.
- It does **not** claim that an element *is* an operator in the quantum sense. The left multiplication is a $\mathbb{C}$-linear map of the algebra, and the interpretation identifies the **process** with that map; whether the map is a quantum channel is a further question, and the completely positive form is read in the $2\times2$ article and not owned here.
- It does **not** claim that a non-invertible map is automatically a measurement. The zero divisors give kernels; a measurement needs a projection onto a state, which is the idempotent side, and the passage from one to the other is the collapse and not the mere vanishing of $\langle\cdot\rangle_{\natural}$.
- It does **not** turn the associativity of the monoid into a physical statement about time ordering. That the composition of the maps is associative is a theorem about composition, true for any algebra; what is read physically is the **order** encoded in $L_{\tilde{Q}_3\tilde{Q}_1}\neq L_{\tilde{Q}_1\tilde{Q}_3}$, not the associativity.

**Open question — which composition is the physical one.** The monoid composes by $L_{\tilde{Q}_3}\circ L_{\tilde{Q}_1}=L_{\tilde{Q}_3\tilde{Q}_1}$, and the corresponding physical statement is that a process followed by a process is their product in that order. Associativity is order-blind, so the composition alone does not fix the order, and the order-sensitive object of the same row is the commutator, its antisymmetric half. **Which of the three — the associative product, its reverse, or the bracket — is the physical composition is open.**

## Physical Readings

The article's interpretation is that the process is the map and the state is the idempotent, and two interpretations follow from it. Read on the clock, the monoid is where a direction of process can live: the sector exchange cannot order the two times because it is invertible and of order four, while an acting map with zero divisors is not invertible, so an arrow is available exactly at the non-units (*Each Sector Is the Other's Clock: the Sector Exchange as Relational Time*). Read on the gauge/state distinction, the monoid is the common home of the reversible group and of the non-invertible projections, which is the framework's reason that a state and a transformation are different kinds of object.

Read as a **thermodynamic arrow**, the split of the monoid into units and non-units is the split between reversible and irreversible operations: the units off the light cone are the reversible maps and the non-invertible maps on it are the irreversible, information-losing ones, so the algebra carries a full arrow rather than a bare reversibility dichotomy. The interpretation is the monoid-level form of the reversible/irreversible dichotomy of *Quantum Channels and the Reversible/Irreversible Dichotomy* and of the information-loss statements of *The Lyapunov Exponent and Information Loss in the Biquaternion Framework*, and the arrow interpretation is the one that *Each Sector Is the Other's Clock* develops.

Read as a **resource theory**, the monoid's split is the framework's version of free and resourceful operations: the units are the free, reversible operations, the non-units the operations that consume a resource, and the states are ordered by the monotones the algebra carries, the norm and the entropy functional, so the monoid is the framework's setting for Landauer-type accounting (*Landauer's Principle and the Material–Informational Exchange in Biquaternionic Form*, *Coarse-Graining and the Biquaternion Entropy Functional*). Boundary: no complete set of monotones and no resource theory in the strict sense is constructed; the interpretation names the shape of the split and not a theorem about it.

Read as a **horizon**, the zero-divisor cone is at once the locus of light, the boundary of the state space and the locus of the non-invertible acting maps, so read physically the cone is where a process loses information: the maps on it are the irreversible ones, and an element of the cone has no inverse on either side. Boundary: the identification of the cone with a horizon is an interpretation and not an entropy; the area law, the temperature and the second law are not supplied by the algebra, whose thermodynamic content is owned by *Landauer's Principle and the Material–Informational Exchange in Biquaternionic Form* and by the KMS articles, and the corpus's own arrow is a dichotomy and not an orientation.

## Summary

An element of the biquaternion algebra generates two $\mathbb{C}$-linear maps, the left multiplication $L_{\tilde{Q}_1}$ and the right multiplication $R_{\tilde{Q}_1}$, with $L_{\tilde{Q}_3}\circ L_{\tilde{Q}_1} = L_{\tilde{Q}_3\tilde{Q}_1}$ and $R_{\tilde{Q}_3}\circ R_{\tilde{Q}_1} = R_{\tilde{Q}_1\tilde{Q}_3}$. The left multiplications form a **monoid** under composition: associative, with identity $L_{e_t}$, closed by the product rule. The element-to-map correspondence is the injective left regular representation, and it is the abstract content of the two matrix operator articles. The units of the monoid are exactly the off-cone elements, the zero divisors are the non-invertible maps, and the light cone is the boundary between them.

The sandwich of the two matrix articles is the composition of a left action with a right action, $\operatorname{H}_{\tilde{Q}_1} = L_{\tilde{Q}_1}\circ R_{\tilde{Q}_1^{*}}$, which is why it is a congruence and not a similarity. The pure states are the rank-one Hermitian idempotents, and idempotent elements are idempotent maps under the injective representation; the Hermitian idempotents lie in $\mathbb{M}_+$ and $\mathbb{M}_-$ has none, the minimal ones are the rank-one Hermitian idempotents, and those are null and sit on the cone. The reading is the process–state split: the process is the map of the monoid, the state is the idempotent, the reversible dynamics is the group of units off the cone, and the measurement is the passage to a non-invertible map on it.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L_{\tilde{Q}_3}$, $R_{\tilde{Q}_3}$ | left and right multiplication by $\tilde{Q}_3$, $L_{\tilde{Q}_3}(\tilde{Q}_2)=\tilde{Q}_3\tilde{Q}_2$, $R_{\tilde{Q}_3}(\tilde{Q}_2)=\tilde{Q}_2\tilde{Q}_3$ |
| $L_{\tilde{Q}_3}\circ L_{\tilde{Q}_1} = L_{\tilde{Q}_3\tilde{Q}_1}$ | the composition rule of the left multiplications |
| $\mathcal{L} = \{L_{\tilde{Q}_1}\}$ | the monoid of left multiplications |
| $L_{e_t}$ | the identity of the monoid |
| $\mathsf{M}_4, \mathsf{M}_4^{R}$ | the regular matrices of the $4\times4$ article |
| $\mathsf{M}_2$, $M = \mathsf{M}_2(\tilde{Q}_1)$ | the matrix image and its matrix |
| $\operatorname{H}_{\tilde{Q}_1} = L_{\tilde{Q}_1}\circ R_{\tilde{Q}_1^{*}}$ | the sandwich as a composition of a left and a right action |
| $\langle\tilde{Q}_1\rangle_{\natural}$ | the biquaternion norm; $\langle\tilde{Q}_1\rangle_{\natural}\neq0$ units, $\langle\tilde{Q}_1\rangle_{\natural}=0$ zero divisors |
| $\tilde{Q}_1^{-1} = \tilde{Q}_1^{\natural}/\langle\tilde{Q}_1\rangle_{\natural}$ | the inverse of a unit |
| $\tilde{\Pi}^2=\tilde{\Pi}$ | an idempotent; a Hermitian idempotent when $\tilde{\Pi}^{*}=\tilde{\Pi}$, the states lying among the Hermitian idempotents of $\mathbb{M}_+$ |

## Further Reading

- *The 2×2 Matrix Operator Representation $M_2(\mathbb{C})\otimes M_2(\mathbb{C})$ of Biquaternions* — the sandwich as the congruence $X\mapsto M X M^{\dagger}$, the completely positive form, and the rank-one collapse.
- *The 4×4 Matrix Operator Representation $M_4(\mathbb{C})$ of Biquaternions* — the sandwich as $L_{\tilde{Q}_1}\circ R_{\tilde{Q}_1^{*}}$ and the regular matrices.
- *The Group of Units of the Biquaternion Algebra and the Complement of the Zero-Divisor Cone* and *The Biquaternioid General Quaternionic Algebra (GQA) over $\mathbb{C}$* — the units, the zero divisors, the inverse $\tilde{Q}_1^{\natural}/\langle\tilde{Q}_1\rangle_{\natural}$ and the light cone.
- *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector* and *Ideals and Peirce Decomposition of the Biquaternion Algebra* — the idempotents, the minimal idempotents and the rank-one projections.
- *The Biquaternioid General Quaternionic Algebra (GQA) over $\mathbb{C}$* — the order of the material composition and the absence of a projection in $\mathbb{M}_-$.
- *Decoherence as Idempotent Projection* — the framework's interpretation of the collapse as an idempotent.
