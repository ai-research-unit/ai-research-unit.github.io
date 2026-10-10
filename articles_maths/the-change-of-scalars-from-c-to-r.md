# __The Change of Scalars from $\mathbb{C}$ to $\mathbb{R}$__

## Introduction

The biquaternion algebra is one ring. Read over $\mathbb{C}$ it is a four-dimensional central simple algebra; read over the subfield $\mathbb{R}$ the same ring is an eight-dimensional simple algebra that is not central. The two readings are not two algebras. They share the additive group, the elements, the product, the identity and every identity of the product; what differs is the field of scalars, and with it the linear structure that the field supports. This article treats the passage between the two readings: which constructions carry one to the other, which statements survive unchanged and which do not, and how the eight real coordinates of the one are related to the four complex coordinates of the other.

The organizing idea is that an algebra structure over a commutative ring $R$ on a ring $A$ is precisely a unital ring homomorphism $R \to Z(A)$ into the centre, the **structure map** of *Algebras: A General Introduction*. The ring $\mathbb{B}$, its product and its elements are fixed once and for all; a field of scalars is the image of such a map, and a change of scalars replaces one image by another inside the same centre. Since the centre of $\mathbb{B}$ is the copy of $\mathbb{C}$ spanned by $e_0$ and $ie_0$, the two admissible structure maps are the inclusion $\mathbb{R} \hookrightarrow \mathbb{C}_{\mathbb{B}}$ and the isomorphism $\mathbb{C} \xrightarrow{\ \sim\ } \mathbb{C}_{\mathbb{B}}$, and among the fields between $\mathbb{R}$ and $\mathbb{C}$ they are the only two: the quaternion ring and the ring $\mathbb{B}$ itself are excluded by the centrality of the image. The passage from $\mathbb{C}$ down to $\mathbb{R}$ is the shrinking of the structure map to a subfield of the centre; the passage back is its enlargement.

Nothing in this article defines the product, the elements or the remarkable subspaces. The product is *The Four General Products of the Biquaternion $\mathbb{C}$ Space*, the real algebra read as an algebra is *Biquaternions as an Algebra over $\mathbb{R}$*, the complex algebra is *Introduction to the General Plain Algebra of Biquaternions*, the vector-space readings are *Biquaternions as a Vector Space over $\mathbb{C}$* and *Biquaternions as a Vector Space over $\mathbb{R}$*, and the two constructions of this article are the general ones of *Change of Rings*, *Extension of Scalars* and *Real Forms and the Descent of an Algebra*. The central element as an operator is $J$, and its linear algebra is that of the vector-space article; it is used here only as the carrier of the difference between the readings.

**Conventions.** $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$. A general element is written $\tilde Q = \sum_{\mu=0}^{3} Q_\mu e_\mu$ with complex coefficients, and equivalently
$$
\tilde Q = \sum_{\mu=0}^{3} q_\mu\, e_\mu + \sum_{\mu=0}^{3} q'_\mu\, (i e_\mu), \qquad q_\mu, q'_\mu \in \mathbb{R} ,
$$
with $Q_\mu = q_\mu + i q'_\mu$. The two scalar systems are named at each step, and a statement is tagged as *about the ring* or *about the scalars*.

## The Same Ring under Two Scalar Systems

**Definition.** A **scalar system** for $\mathbb{B}$ is a unital ring homomorphism $\varphi : k \to Z(\mathbb{B})$ from a field $k$ into the centre. The field $k$ is then the field of scalars of the reading, the product is $k$-bilinear through the centrality of $\varphi(k)$, and $\mathbb{B}$ is a $k$-algebra.

**Proposition.** The scalar systems of $\mathbb{B}$ over the subfields $k$ of $\mathbb{C}$ with $\mathbb{R} \subseteq k \subseteq \mathbb{C}$ are exactly two, the real one and the complex one.

**Proof.** The centre is $Z(\mathbb{B}) = \mathbb{C}_{\mathbb{B}} = \mathbb{C} e_0$, a copy of the field $\mathbb{C}$ inside $\mathbb{B}$. A unital homomorphism from a field into the commutative ring $\mathbb{C}$ is injective, and the image is a subfield of $\mathbb{C}$; the only subfields between $\mathbb{R}$ and $\mathbb{C}$ are $\mathbb{R}$ itself and $\mathbb{C}$ itself. (Without the hypothesis that $\mathbb{R} \subseteq k$ there are others, one for every subfield of $\mathbb{R}$, and the proposition would fail; the two readings of the article are the intermediate ones.) A homomorphism from $\mathbb{H}$ cannot exist, and the same holds for $\mathbb{B}$ in place of $\mathbb{H}$: the target is commutative and the source is not, so there is no unital homomorphism at all. $\square$

**Remark (the two complex structures).** The complex scalar system is fixed by the isomorphism $\mathbb{C} \xrightarrow{\ \sim\ } \mathbb{C}_{\mathbb{B}}$ together with the choice of the element that is to be the scalar $i$. The only other choice is $-i$, giving the conjugate isomorphism $\lambda \mapsto \bar\lambda$ and the complex structure $-J$, and the two choices are exchanged by the complex conjugation $c$ of the ring (*Introduction to the General Plain Algebra of Biquaternions*, §*The Gate: a Central Element of Square $-1$*: the complex structure is a central element $j$ with $j^2 = -e_0$, and $j = \pm i$). The proposition above therefore counts the two subfields of the centre; the complex one carries the two conjugate structure maps, and they define the same reading of the ring.

The two systems are the identity of $\mathbb{C}$ and the inclusion of $\mathbb{R}$. The ring-theoretic content of $\mathbb{B}$ is the same in both: the same addition, the same multiplication, the same $e_0$, the same elements $i$ and $e_k$. What the complex system has and the real system lacks is the requirement that the product be linear over a two-dimensional scalar field.

**Remark (the same ring, not two algebras).** The phrase "the change of scalars" names a change in the structure map and not in the ring. The set of elements is unchanged, the graphs of addition and multiplication are unchanged, and the identity is unchanged; only the set of linear combinations that the scalars permit is enlarged or reduced. An identity such as $e_1e_2 = e_3$ or $i^2 = -e_0$ is an identity of the ring and holds in both readings; the statement "$\mathbb{B}$ is four-dimensional" is a statement about the scalars and holds in one.

## Restriction of Scalars and the Real Reading

The passage from the complex reading to the real reading is a **restriction of scalars** along $\mathbb{R} \hookrightarrow \mathbb{C}$ (*Change of Rings*, §*Restriction of Scalars*).

**Theorem.** Every $\mathbb{C}$-algebra is an $\mathbb{R}$-algebra by restriction of scalars along the inclusion $\mathbb{R} \subset \mathbb{C}$, with the same addition, the same product and the same elements; if the complex dimension is $n$, the real dimension is $2n$.

**Proof.** Given the complex structure map $\mathbb{C} \to Z(\mathbb{B})$, its composite with the inclusion $\mathbb{R} \subset \mathbb{C}$ is a real structure map; the axioms of a module over a ring are satisfied by the same operations, and $\mathbb{B}$ as a real vector space has the real basis $e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3$, the complex basis followed by its image under $J$. $\square$

So the real reading of $\mathbb{B}$ is the restriction $\operatorname{Res}_{\mathbb{C}/\mathbb{R}} \mathbb{B}$, of real dimension $8 = 2 \cdot 4$: the real basis is $e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3$, twice the complex basis $e_0,e_1,e_2,e_3$. Restriction is exact and faithful on modules, and every $\mathbb{C}$-linear map is $\mathbb{R}$-linear, so no structure is lost in the passage down: the real reading sees everything the complex reading sees, and more. Nothing is created either: an element of $\mathbb{B}$ has four complex coordinates in the complex reading and eight real coordinates in the real reading, and the eight are the four, split.

## Extension of Scalars and the Real Forms

The passage in the other direction is an **extension of scalars**, and it has two forms that must not be confused because they give different algebras.

**The extension of the real reading.** The extension of the eight-dimensional real algebra $\mathbb{B}$ along $\mathbb{R} \subset \mathbb{C}$ is the complex algebra $\mathbb{C} \otimes_{\mathbb{R}} \mathbb{B}$, of complex dimension $8$. It is *not* the complex reading of $\mathbb{B}$: the complex reading is four-dimensional. Its structure is computed in *Biquaternions as an Algebra over $\mathbb{R}$*, §*The Complexification Is Not the Complex Algebra*, where $\mathbb{C} \otimes_{\mathbb{R}} \mathbb{B} \cong \mathbb{B} \oplus \mathbb{B}$ is shown; the complexification of the real algebra is a larger algebra, a product of two copies of the complex reading.

**The extension of a real form.** The complex reading is instead recovered from a **real form**: a real *subalgebra* $V \subset \mathbb{B}$, of real dimension four, with $\mathbb{B} = V \oplus JV$ for $J(\tilde Q) = i\tilde Q$. The closure of $V$ under the product is what makes the multiplication of $\mathbb{B}$ restrict to a real algebra structure on $V$, and then the map
$$
\mathbb{C} \otimes_{\mathbb{R}} V \longrightarrow \mathbb{B}, \qquad z \otimes v \longmapsto zv ,
$$
is an isomorphism of complex algebras: $\mathbb{C} \otimes_{\mathbb{R}} V \cong \mathbb{B}$. This is the meaning of *real form* in *Real Forms and the Descent of an Algebra*, where a real form of a complex algebra is a real subalgebra whose complexification is the algebra. The standard example is the quaternion subspace $\mathbb{H}_{\mathbb{B}} = \operatorname{span}_{\mathbb{R}}\{e_0,e_1,e_2,e_3\}$, whose extension of scalars is $\mathbb{C} \otimes_{\mathbb{R}} \mathbb{H} = \mathbb{B}$. The choice of a real form is data beyond the real reading.

The closure hypothesis cannot be dropped. A real subspace $V$ of dimension four with $V \cap JV = 0$ satisfies $\mathbb{B} = V \oplus JV$, so it is a real form of the underlying complex *vector* space (*Biquaternions as a Vector Space over $\mathbb{R}$*, §*The Real Form*), but it need not be a subalgebra and then it does not recover the complex *algebra*: for $V = \operatorname{span}_{\mathbb{R}}\{e_0, e_1, e_2, ie_3\}$ one has $V \cap JV = 0$ and $\mathbb{B} = V \oplus JV$, yet $e_1e_2 = e_3 \notin V$.

**Remark (the two dimensions eight and four).** The two extension constructions are distinguished by the dimension of the algebra one starts from. The real reading, of real dimension eight, extends to a complex algebra of complex dimension eight; a real form, of real dimension four, extends to the complex reading, of complex dimension four. The operator $J$, not a scalar extension, is what recovers the complex action from the eight-dimensional real reading; the scalar extension recovers the complex reading only after a real form has been chosen.

## Statements About the Ring and Statements About the Scalars

The two readings agree on everything that is a property of the ring, and they differ on everything that mentions the scalar field or the linear structure it supports. The criterion is the language in which the statement is made.

**Theorem (the criterion).** A statement is *about the ring*, and therefore has the same truth value in the two readings, when it is expressed using the ring operations, the identity and quantification over elements of $\mathbb{B}$ alone. A statement is *about the scalars*, and may change, when it mentions the field of scalars, a dimension over that field, a linear map required to be scalar-linear, or a tensor product over that field.

**Proof.** A change of scalars replaces the structure map $k \to Z(\mathbb{B})$; it leaves the additive group and the product untouched. Every statement built from the operations of the ring is evaluated on that same group and product and so is unchanged. A statement that names $k$, or counts a $k$-basis, or asserts that a map is $k$-linear, is evaluated against the structure map and may change with it. $\square$

**The ring-level statements.** The following are statements about the ring and hold identically in the two readings; the first group is proved in the articles named and is not repeated here.

- The multiplication table of the eight basis elements, the associativity, the two-sided unit $e_0$, non-commutativity (*Biquaternions as an Algebra over $\mathbb{R}$*).
- The centrality of $i$, the relation $i^2 = -e_0$, and the identification of the centre with $\mathbb{C}_{\mathbb{B}}$ (*Introduction to the General Plain Algebra of Biquaternions*).
- The four conjugations ${}^{\natural}$, $\bar{\cdot}$, ${}^{*}$, ${}^{\flat}$ as maps of the ring, their orders and the group they generate; only their scalar-linearity changes (*The Group of Involutions*).
- The **lattice of ideals**, including simplicity: the two-sided ideals are $0$ and $\mathbb{B}$, and the minimal left ideals are parametrized by $\mathbb{P}^1(\mathbb{C})$, in both readings (*Biquaternion Ideals and Peirce Decomposition*, §*The Real Structure*).
- The **idempotents**: the equation $\tilde\Pi^2 = \tilde\Pi$ is a ring equation, so the idempotents, their classification and the bijection with the roots of $-1$ are the same sets (*Biquaternion Idempotents and Projections*).
- The **zero divisors**: $\tilde Q$ is a zero divisor exactly when $\tilde Q\tilde Q^{\natural} = 0$, a ring equation, so the zero-divisor cone and its two families are the same sets (*Biquaternion Zero Divisors*).
- **Invertibility**: $\tilde Q$ is invertible exactly when $\tilde Q\tilde Q^{\natural} \neq 0$; the criterion is a ring criterion, and the group of units is the same set (*Biquaternion Norm and Invertibility*).

**The scalar-level statements.** The following mention the scalars and differ between the readings.

- The **dimension**: four over $\mathbb{C}$, eight over $\mathbb{R}$.
- **Central simplicity**: $\mathbb{B}$ is central simple over $\mathbb{C}$, with centre exactly the scalars; over $\mathbb{R}$ it is simple but not central, and its complexification splits, since $\mathbb{C} \otimes_{\mathbb{R}} \mathbb{B} \cong \mathbb{B} \oplus \mathbb{B}$.
- The **real-linear maps**: $\operatorname{End}_{\mathbb{C}}(\mathbb{B}) \cong M_4(\mathbb{C})$ against $\operatorname{End}_{\mathbb{R}}(\mathbb{B}) \cong M_8(\mathbb{R})$, of real dimensions $32$ and $64$.
- The **subalgebras**: a real subspace closed under the product need not be a complex subspace, so the real reading has more subalgebras than the complex reading (*The Real Subalgebras of the Biquaternion Algebra*).
- The **automorphisms and derivations**: the automorphism group is strictly larger over $\mathbb{R}$, while the derivation space coincides (*The Automorphisms and Derivations of the Real Biquaternion Algebra*).

The first two groups are not independent of the structure of the ring; the point of the criterion is that the split is systematic. A statement of the first group can be *transported* to the second reading by restriction or extension of scalars without re-derivation; a statement of the second group cannot.

## The Two Coordinate Systems and the Passage Between Them

### The Coordinates

The complex reading writes an element in the four complex coordinates $(Q_0,Q_1,Q_2,Q_3)$ on the complex basis $e_0,e_1,e_2,e_3$, with $Q_\mu = q_\mu + i q'_\mu$. The real reading writes the same element in the eight real coordinates
$$
(q_0,q_1,q_2,q_3,q'_0,q'_1,q'_2,q'_3)
$$
on the real basis $e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3$; the two coordinate systems are those of *Biquaternions as a Vector Space over $\mathbb{C}$* and *Biquaternions as a Vector Space over $\mathbb{R}$*.

**Proposition (the passage).** The passage from the four complex coordinates to the eight real coordinates is the separation of each complex coordinate into its real and imaginary parts; the passage back is the pairing of the two halves.

**Proof.** The identity $Q_\mu = q_\mu + i q'_\mu$ separates the coefficient in the complex line $\mathbb{C} e_\mu$ into the two real directions $e_\mu$ and $ie_\mu$; reading the four lines gives the eight coordinates, and reading the two halves of each line gives the four. $\square$

### The Passage Is Forgetting the Complex Action

The passage is not merely a reshuffling of coordinates: it is the forgetting of the $\mathbb{C}$-action on the algebra. Under the complex structure map, the scalar $i \in \mathbb{C}$ acts on $\mathbb{B}$ by left multiplication by the central element $i = ie_0$, the operator $J$. The relation
$$
\lambda \tilde Q = a \tilde Q + b J(\tilde Q), \qquad \lambda = a + bi ,
$$
is the complex action written in real terms: the complex structure is the real linear structure together with $J$, and the passage from the complex reading to the real reading is the forgetting of $J$. Conversely, the real reading together with $J$ is the complex reading. The operator $J$ is real-linear with $J^2 = -\mathrm{id}$, and it commutes with the product, $J(\tilde P\tilde Q) = J(\tilde P)\tilde Q = \tilde P J(\tilde Q)$, because $i$ is central. It is $\mathbb{C}$-linear, but it is not a ring automorphism: $J(\tilde P\tilde Q) = i\tilde P\tilde Q$ while $J(\tilde P)J(\tilde Q) = -\tilde P\tilde Q$. This is the content of *Biquaternions as a Vector Space over $\mathbb{R}$*, §*The Complex Structure*, and it is the reason the passage is reversible: $J$ is available inside the ring, as the operator of left multiplication by the element $i$.

**Proposition (the passage in one line).** The complex reading is the real reading together with the operator $J$, and the real reading is the complex reading with $J$ forgotten:
$$
\text{complex reading} \;=\; (\text{real reading},\, J), \qquad \text{real reading} \;=\; \operatorname{Res}_{\mathbb{C}/\mathbb{R}}\bigl(\text{complex reading}\bigr).
$$

## The Central Element as the Carrier of the Difference

The whole of the difference between the two readings is carried by one element of the ring, the central element $i$. Two consequences of its centrality make this precise, and they are the reason the scalar-level group of the previous section is exactly what it is.

**First, the central element supplies the missing scalar action.** A map $T$ of $\mathbb{B}$ is $\mathbb{C}$-linear exactly when it commutes with $J$ and $\mathbb{C}$-antilinear exactly when it anticommutes with it; the quaternion conjugation $\natural$ commutes and the other maps anticommute. This is the *commutator with $J$* criterion of *Biquaternions as a Vector Space over $\mathbb{R}$*, §*The Complex Structure*. A map that is only $\mathbb{R}$-linear may lie on either side, and it is precisely the maps on the anticommuting side that the complex reading does not see and the real reading does.

**Second, the central element makes every ring condition a complex condition.** Because $i$ is central and lies in $\mathbb{B}$, left multiplication by $i$ is left multiplication by an element of the ring. Hence any additive subgroup closed under left multiplication by $\mathbb{B}$ is automatically a complex subspace, and any equation in the ring is an equation whose coefficients may be taken complex. This is why the ideals, the idempotents and the zero divisors of the ring-level list cannot change between the readings; the argument is the subject of *Why the Ideals, the Idempotents and the Zero Divisors Do Not Change*.

**Remark (what the centrality does not do).** Centrality of $i$ makes the ring conditions insensitive to the scalars; it does not make the *linear* conditions insensitive. The real dimension of the ring, the real-linear maps that anticommute with $J$, and the real subalgebras that meet $JV$ trivially are all sensitive to the scalars, because they are conditions on the real vector space and not on the ring. The distinction between the two groups of the previous section is exactly the distinction between the conditions that the central element forces and those that it does not.

## What the Change of Scalars Moves

| structure | over $\mathbb{C}$ | over $\mathbb{R}$ |
|---|---|---|
| the ring $\mathbb{B}$ | the same | the same |
| dimension | $4$ | $8$ |
| central simple | yes | no: simple, centre $\mathbb{C} \neq \mathbb{R}$ |
| two-sided ideals | $0$, $\mathbb{B}$ | $0$, $\mathbb{B}$ |
| minimal left ideals | $\mathbb{P}^1(\mathbb{C})$ | the same sets |
| idempotents | classified by the roots of $-1$ | the same set |
| zero-divisor cone | complex dimension $3$ | real dimension $6$, the same set |
| units | $\tilde Q\tilde Q^{\natural} \neq 0$ | the same set |
| linear self-maps | $M_4(\mathbb{C})$, real dimension $32$ | $M_8(\mathbb{R})$, real dimension $64$ |
| subalgebras | complex subspaces, even real dimension | real subspaces, no parity restriction |
| automorphism group | inner, complex dimension $3$ | $\mathrm{Aut}_{\mathbb{C}} \rtimes \mathbb{Z}/2$, two components |
| derivation space | complex dimension $3$ | the same space, real dimension $6$ |

The table is the summary of the criterion. Its rows about the ring — the ring itself, the ideals, the idempotents, the zero divisors and the units — are the rows the reader may verify by transporting them along the restriction of scalars. Its rows about the scalars — the dimension, central simplicity, the linear maps, the subalgebras, the automorphisms and the derivations — are each treated in its own article, and the derivation row is the one place where the two fields give the same object for a reason and not by coincidence, because the centre $\mathbb{C}$ has no nonzero derivation over $\mathbb{R}$.

## Summary

The biquaternion ring is one ring under two scalar systems, the complex one and the real one, related as the image of a structure map $\mathbb{C} \to Z(\mathbb{B})$ and its restriction to the subfield $\mathbb{R}$. The real reading is the restriction of scalars of the complex reading, of doubled dimension; the complex reading is recovered from the real reading either by adjoining the operator $J$ of left multiplication by $i$, or, starting from a real form such as the quaternion subspace, by extension of scalars.

$$
\boxed{\ \text{One ring; two structure maps } \mathbb{R} \hookrightarrow \mathbb{C}_{\mathbb{B}} \text{ and } \mathbb{C} \xrightarrow{\sim} \mathbb{C}_{\mathbb{B}} \text{; the passage is the structure map.}\ }
$$

Everything that is a statement about the ring — the multiplication, the identity, the centrality of $i$, the conjugations, the ideals, the idempotents, the zero divisors, the units — is the same in the two readings. Everything that is a statement about the scalars — the dimension, central simplicity, the linear maps, the subalgebras, the automorphisms and, in one row only, the derivations — may differ, and the central element $i$ is the carrier of the difference. The eight real coordinates are the four complex ones separated, and the operator $J$ is what has been forgotten in the separation and what must be adjoined to recover the complex reading.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{Res}_{\mathbb{C}/\mathbb{R}} \mathbb{B}$ | the real reading: the same ring over the scalars $\mathbb{R}$, dimension $8$ |
| $\mathbb{C} \otimes_{\mathbb{R}} \mathbb{B}$ | the complexification of the real reading, $\cong \mathbb{B} \oplus \mathbb{B}$, dimension $8$ over $\mathbb{C}$ |
| $\mathbb{C} \otimes_{\mathbb{R}} V$ | the extension of scalars of a real form $V$, $\cong \mathbb{B}$ |
| $J : \tilde Q \mapsto i\tilde Q$ | the complex structure, $J^2 = -\mathrm{id}$, the complex action read over $\mathbb{R}$ |
| $(Q_0,Q_1,Q_2,Q_3)$ | the four complex coordinates, $Q_\mu = q_\mu + iq'_\mu$ |
| $(q_0,q_1,q_2,q_3,q'_0,q'_1,q'_2,q'_3)$ | the eight real coordinates |
| $\varphi : k \to Z(\mathbb{B})$ | the structure map of the scalar system $k$ |
| $Z(\mathbb{B}) = \mathbb{C}_{\mathbb{B}}$ | the centre, a copy of $\mathbb{C}$; the scalar image |
| $V$ | a real form: a real four-dimensional subalgebra with $\mathbb{B} = V \oplus JV$ |

## Further Reading

- *Introduction to the General Plain Algebra of Biquaternions* (`articles_maths/introduction-to-the-general-plain-algebra-of-biquaternions.md`), for the complex reading, the structure map and central simplicity.
- *Biquaternions as an Algebra over $\mathbb{R}$* (`articles_maths/biquaternions-as-an-algebra-over-r.md`), for the real algebra, the dimension count and the complexification.
- *Change of Rings* (`articles_maths/change-of-rings.md`) and *Extension of Scalars* (`articles_maths/extension-of-scalars.md`), for restriction and extension in general.
- *Real Forms and the Descent of an Algebra* (`articles_maths/real-forms-and-the-descent-of-an-algebra.md`), for the correspondence between real forms and conjugations.
- Nicolas Bourbaki, *Algebra I* (Springer, 1998), for algebras over a commutative ring, the structure map into the centre and the tensor product of algebras.
- Tsit-Yuen Lam, *A First Course in Noncommutative Rings* (Springer, 2nd ed. 2001), for the centre and the scalar extension of a simple algebra.
- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for restriction and extension of scalars.
