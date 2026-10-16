# __The Four General Products and the Degree-2 Forms of the Biquaternion Space__

## Introduction

The biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ carries four multiplications on its underlying complex vector space, the **four general products**, and each of them carries a **degree-two form**, its scalar part. This article is the first of the three reader articles of the band *Focus on Biquaternioid structures*: it reads the four general products and the four scalar forms they carry, while the second reads the twelve products the four split into and the third reads the four forms and the four algebraic norms on the remarkable subspaces and under the change of scalars.

The four general products are the source of the whole band. The twelve products of *The Twelve Products and the Twelve Algebraic Structures* are the four general products together with their eight parts, and the four forms are the scalar parts of the four general products. Nothing here is proved anew. The products are the matter of *The Four General Products of the Biquaternioid $\mathbb{C}$ Space*, *Relations Between the Four General Products*, *Comparison Between the Four General Products* and *The Four General Products and Operators*; the forms are the matter of *The 4 Forms over the Biquaternioid $\mathbb{C}$ Space*, their algebraic norms of *The 4 Algebraic Norms over the Biquaternioid $\mathbb{C}$ Space*, and the two on the subspaces of *Remarkable Subspaces and the Four General Products* and *Remarkable Subspaces and the Four Forms*.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_0=1,e_1,e_2,e_3$, the relations $e_k^{2}=-e_0$ and $e_1e_2=e_3$, $e_2e_3=e_1$, $e_3e_1=e_2$, and central scalar imaginary $i$ with $i^{2}=-1$. A general element is $\tilde Q=\sum_{\mu=0}^{3}Q_\mu e_\mu=Q_0e_0+\vec Q$, with complex coefficients $Q_\mu$ and vector part $\vec Q=\sum_{k=1}^{3}Q_ke_k$. The natural conjugation ${}^{\natural}$ fixes $i$ and negates $e_1,e_2,e_3$; the coefficientwise conjugation $\bar{\cdot}$ conjugates the four coefficients; the Hermitian conjugation is ${}^{*}=\bar{\cdot}\circ{}^{\natural}$, so that $Q^{*}_\nu=\varepsilon_\nu\overline{Q_\nu}$ with $\varepsilon=(1,-1,-1,-1)$. The scalar part is $\mathrm{Sc}(\tilde X)=X_0$ and the trace is $\mathrm{Tr}=2\,\mathrm{Sc}$. The complex bilinear dot product and cross product of the vector parts are $(\vec P,\vec Q)=\sum_kP_kQ_k$ and $\vec P\times\vec Q$, and $\overline{\vec Q}$ is the coefficientwise conjugate of the vector part. The remarkable subspaces are the centre $\mathbb{C}_{\mathbb{B}}$, the vector subspace $\mathrm{Vect}(\mathbb{B})$, the quaternion and antiquaternion subspaces $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, and the Hermitian and anti-Hermitian subspaces $\mathbb{M}_+$, $\mathbb{M}_-$. All conventions, including the reading of the four pairings with one bracket, are those of *Conventions in the Biquaternion Universe*.

## The Four General Products

**Definition (the four general products).** The four general products are the four rules

$$
\tilde P\tilde Q , \qquad \tilde P\tilde Q^{*} , \qquad \tilde P^{\natural}\tilde Q , \qquad \tilde P^{\natural}\tilde Q^{*} ,
$$

the **general plain bilinear**, the **general plain sesquilinear**, the **general quaternionic bilinear** and the **general quaternionic sesquilinear** product.

**One multiplication table, two insertions.** The four rules multiply the coordinates of the two elements on the same products $e_\mu e_\nu$ of the basis, and they differ in one point alone: whether the first element is read as it stands or through ${}^{\natural}$, and whether the second is read as it stands or through ${}^{*}$, the two choices made independently. The four are therefore the orbit

$$
\tilde P\star\tilde Q=K_1(\tilde P)\,K_2(\tilde Q),\qquad K_1\in\{\mathrm{id},{}^{\natural}\},\quad K_2\in\{\mathrm{id},{}^{*}\},
$$

of one rule under the insertion of a conjugation into a slot. Nothing else varies, and ${}^{*}$ is never put in the first slot nor ${}^{\natural}$ in the second.

**The scalar–vector forms.** Written on the coordinates of the two elements,

$$
\tilde P\tilde Q=\bigl[P_0Q_0-(\vec P,\vec Q)\bigr]+P_0\vec Q+Q_0\vec P+\vec P\times\vec Q,
$$

$$
\tilde P\tilde Q^{*}=\bigl[P_0\overline{Q_0}+(\vec P,\overline{\vec Q})\bigr]-P_0\overline{\vec Q}+\overline{Q_0}\vec P-\vec P\times\overline{\vec Q},
$$

$$
\tilde P^{\natural}\tilde Q=\bigl[P_0Q_0+(\vec P,\vec Q)\bigr]+P_0\vec Q-Q_0\vec P-\vec P\times\vec Q,
$$

$$
\tilde P^{\natural}\tilde Q^{*}=\bigl[P_0\overline{Q_0}-(\vec P,\overline{\vec Q})\bigr]-P_0\overline{\vec Q}-\overline{Q_0}\vec P+\vec P\times\overline{\vec Q}.
$$

The two bilinear products are $\mathbb{C}$-bilinear in both slots; the two sesquilinear products are $\mathbb{C}$-linear in the first slot and conjugate-linear in the second. No two of the four agree on every pair.

**The two slot rules.** The **second slot** decides whether the operation is a **composition** or a **pairing**. Read without a conjugation it is $\mathbb{C}$-bilinear and can be iterated, which is the two **general algebras** over $\mathbb{C}$; read with the star it is sesquilinear over $(\mathbb{C},\bar{\cdot})$ and can only be evaluated, which is the two **general sesqualgebras**. The **first slot** decides whether the scalar form is definite on each sector or carries a signature: the two products whose first slot is read as it stands, the general plain bilinear and the general plain sesquilinear, have forms definite on each sector — the sector sign $\langle\cdot,\cdot\rangle$ and the Born form $\langle\cdot,\cdot\rangle_{*}$ — while the two whose first slot carries ${}^{\natural}$, the general quaternionic products, have forms indefinite on each sector — the interval $\langle\cdot,\cdot\rangle_{\natural}$ and the Krein form $\langle\cdot,\cdot\rangle_{\natural*}$. It is the first slot that decides which of the four measures on a sector and which carries a metric with a light cone. The coefficientwise twist $\varepsilon_\mu$ of the scalar form is a separate matter, decided by the two slots together: it is present when the two slots are treated alike, neither conjugated (the general plain bilinear $\langle\cdot,\cdot\rangle$) or both conjugated (the general quaternionic sesquilinear $\langle\cdot,\cdot\rangle_{\natural*}$), and absent when exactly one is conjugated (the general quaternionic bilinear $\langle\cdot,\cdot\rangle_{\natural}$ and the general plain sesquilinear $\langle\cdot,\cdot\rangle_{*}$).

## Relations Between the Four

The four general products are not four unrelated rules: the two insertions are independent, and every link between the four is a consequence of that single distinction. The two conjugations separate the scalar part of a factor from its vector part, by the splitting identities

$$
\tilde P\tilde Q\pm\tilde P^{\natural}\tilde Q=2P_0\tilde Q \ \text{and}\ 2\vec P\tilde Q,
\qquad
\tilde P\tilde Q^{*}\pm\tilde P^{\natural}\tilde Q^{*}=2P_0\tilde Q^{*}\ \text{and}\ 2\vec P\tilde Q^{*},
$$

and the same two identities hold with the two vector parts in place of the scalar parts. The ${}^{\natural}$ of the quaternionic product and the ${}^{*}$ of the sesquilinear product return a product with the slots exchanged, which is why the scalar parts of the two are symmetric and conjugate-symmetric respectively, while no one of the four general products is commutative. The two remaining conjugations of the algebra add no new scalar part: $\mathrm{Sc}(\bar{\tilde P}\tilde Q)=\mathrm{Sc}(\tilde Q^{\natural}\tilde P^{*})$ and $\mathrm{Sc}(\tilde P\bar{\tilde Q})=\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})$.

**Comparison.** Of the four, exactly one is **associative**: the general plain bilinear product. The unit $e_0$ is two-sided for the general plain bilinear product, **right** for the general plain sesquilinear product, **left** for the general quaternionic bilinear product, and **absent** for the general quaternionic sesquilinear product. No one of the four is commutative, and none has a two-sided unit other than the plain one. The four differ in the class of the operation — the two algebras over $\mathbb{C}$ against the two sesqualgebras over $(\mathbb{C},\bar{\cdot})$ — and in the pairing they carry, not in the multiplication table of the units, which is the same in all four.

## The Degree-2 Forms the Four Products Carry

The scalar part of a general product is a form of degree two in the pair of its arguments, and the four scalar parts are the four **forms** of the algebra. With the one bracket of *Conventions in the Biquaternion Universe* whose subscript names the inserted conjugation,

$$
\langle\tilde P,\tilde Q\rangle=\mathrm{Sc}(\tilde P\tilde Q)=\textstyle\sum_\mu\varepsilon_\mu P_\mu Q_\mu,
\qquad
\langle\tilde P,\tilde Q\rangle_{*}=\mathrm{Sc}(\tilde P\tilde Q^{*})=\textstyle\sum_\mu P_\mu\overline{Q_\mu},
$$

$$
\langle\tilde P,\tilde Q\rangle_{\natural}=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)=\textstyle\sum_\mu P_\mu Q_\mu,
\qquad
\langle\tilde P,\tilde Q\rangle_{\natural*}=\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})=\textstyle\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}.
$$

They are named the **general plain bilinear** form $\langle\cdot,\cdot\rangle$, the **general plain sesquilinear** or **Hermitian** form $\langle\cdot,\cdot\rangle_{*}$, the **general quaternionic bilinear** form $\langle\cdot,\cdot\rangle_{\natural}$, and the **general quaternionic sesquilinear** or **Krein** form $\langle\cdot,\cdot\rangle_{\natural*}$; their values are the jobs of composition, probability, causality and gauge. The four are **one bilinear form read through the two involutions**,

$$
\langle\tilde P,\tilde Q\rangle_{*}=\langle\tilde P,\tilde Q^{*}\rangle,\qquad
\langle\tilde P,\tilde Q\rangle_{\natural}=\langle\tilde P^{\natural},\tilde Q\rangle,\qquad
\langle\tilde P,\tilde Q\rangle_{\natural*}=\langle\tilde P^{\natural},\tilde Q^{*}\rangle,
$$

so that the four forms are not four computations but one computation in the four insertions of the grid. The two bilinear forms $\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{\natural}$ are symmetric and $\mathbb{C}$-bilinear, the two sesquilinear forms $\langle\cdot,\cdot\rangle_{*}$ and $\langle\cdot,\cdot\rangle_{\natural*}$ conjugate-symmetric and sesquilinear: $\langle\tilde P,\tilde Q\rangle_{*}=\overline{\langle\tilde Q,\tilde P\rangle_{*}}$ and $\langle\tilde P,\tilde Q\rangle_{\natural*}=\overline{\langle\tilde Q,\tilde P\rangle_{\natural*}}$.

**The four algebraic norms.** The **algebraic norm** of a form is its algebraic norm, the degree-two function of one element,

$$
\langle\tilde Q\rangle=Q_0^{2}-\textstyle\sum_kQ_k^{2},\qquad
\langle\tilde Q\rangle_{*}=\textstyle\sum_\mu\lvert Q_\mu\rvert^{2},\qquad
\langle\tilde Q\rangle_{\natural}=Q_0^{2}+\textstyle\sum_kQ_k^{2},\qquad
\langle\tilde Q\rangle_{\natural*}=\lvert Q_0\rvert^{2}-\textstyle\sum_k\lvert Q_k\rvert^{2}.
$$

Two of the four have a sense the others lack, and the two senses are not the same sense. **$\langle\cdot,\cdot\rangle_{*}$ is positive definite**: $\langle\tilde Q\rangle_{*}>0$ for $\tilde Q\neq0$, it is real on every element, and it is the unique topological norm of the space, its square root being the Euclidean norm. **$\langle\cdot,\cdot\rangle_{\natural}$ is multiplicative**: on the general quaternionic bilinear product,

$$
\langle\tilde P^{\natural}\tilde Q\rangle_{\natural}=\langle\tilde P\rangle_{\natural}\,\langle\tilde Q\rangle_{\natural},
$$

so the units and the zero divisors of that product are closed under it, and the norm behaves as a charge of the composition rather than as a length; it is the norm of no other product. $\langle\cdot,\cdot\rangle_{*}$ is the only one of the four that is definite on each of the remarkable subspaces; the other three are indefinite on the whole algebra, $\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{\natural}$ as complex bilinear forms of rank four and $\langle\cdot,\cdot\rangle_{\natural*}$ as an indefinite Hermitian form. This is the separation of the **multiplicative** sense of a norm from the **positive definite** sense, and it is one of the things the remarkable subspaces measure.

## The Four General Products and Their Operators

Each general product gives its elements two families of operators, the left and the right multiplications, and the four products give four such families. The passage from the product to its operators is the passage from a pairing to an adjoint, and it is worth stating what the product does and does not decide. It **decides the pairing**, hence the adjoint, hence the name of the family: the plain bilinear product gives the association family, the general plain sesquilinear product the Hermitian adjoint family, the general quaternionic bilinear product the signed inner conjugation family, and the general quaternionic sesquilinear product the Krein form, which carries its own indefinite theory rather than a family of the four-adjoint kind. It does **not** decide the action: whether an element acts as a rotation or as a reflection is decided by the element and by the inserted sign, and the inserted sign is a choice among the involutions the algebra already carries. The qualification is that the choice is not arbitrary: on the vector subspace the plain product cannot produce a reflection, only its negative, so one insertion is forced by the algebra and not merely preferred.

The left multiplications of the four are the general plain bilinear ones read through the conjugations,

$$
L^{\natural}_{\tilde P}=L_{\tilde P^{\natural}},\qquad
L^{*}_{\tilde P}=(\cdot)^{*}\circ R_{\tilde P^{*}},\qquad
L^{\natural*}_{\tilde P}=(\cdot)^{*}\circ R_{\bar{\tilde P}},
$$

so that the general plain bilinear and the general quaternionic bilinear products have a monoid of left multiplications, and the two sesquilinear products do not. The adjoint of a multiplication for the trace form is the multiplication by the star-conjugate, $(L_{\tilde A})^{\dagger}=L_{\tilde A^{*}}$, the trace form being $\mathrm{Tr}(\tilde P\tilde Q)=2\,\mathrm{Sc}(\tilde P\tilde Q)$. The reading of the operators of the four products is *The Four General Products and Operators*, and the family names are read in *The Four Adjoints of the Two Algebras and the Two Sesqualgebras in Examples*.

## The Four Products on the Remarkable Subspaces

The four general products do not behave alike on the six remarkable subspaces, and the two facts that matter for the band are the **closure** and the **part that lands in a subspace**.

**Closure.** All four general products keep a subspace inside itself for exactly **two** of the six: the centre $\mathbb{C}_{\mathbb{B}}$ and the quaternion subspace $\mathbb{H}_{\mathbb{B}}$. On the centre the four give the field $\mathbb{C}$; on the quaternion subspace the general plain product gives a copy of the real quaternion algebra, whose symmetrisation is a Jordan algebra. On the other four subspaces — the vector subspace, the antiquaternion subspace and the two sectors — no one of the four keeps the subspace inside itself. The two complex subspaces, the centre and the vector subspace, are the ones multiplication by $i$ preserves; the four real-type subspaces, the quaternion and antiquaternion subspaces and the two sectors, are the ones it exchanges in pairs, and the exchange is what moves a product out of its subspace.

**The parts and the subspaces.** The two halves of a product land in the remarkable subspaces, and the pattern is the same for all four general products: the **symmetrisation** of every one of the four stays inside exactly the centre, the quaternion subspace and the Hermitian subspace, and the **bracket** of every one of the four stays inside exactly the centre and the quaternion subspace, the two bilinear brackets also staying inside the vector subspace and the general plain sesquilinear bracket also inside the anti-Hermitian subspace. Whether the closed operation then satisfies its identity decides the algebra. **Three subspaces are Jordan algebras**: the centre, for the general plain and the general quaternionic bilinear product, which coincide there and give the field $\mathbb{C}$; the quaternion subspace, for the general plain product, giving the symmetrised real quaternion algebra; and the Hermitian subspace, for the general plain bilinear and the general plain sesquilinear product, which coincide there, giving the Hermitian Jordan algebra of degree two. **Four are Lie algebras**: the centre, for all four products, abelian for the two bilinear and the two-dimensional non-abelian algebra for the two sesquilinear; the vector subspace, for the two bilinear brackets, the complex Lie algebra $\mathfrak{sl}(2,\mathbb{C})$; the quaternion subspace, for the general plain bilinear and the general quaternionic sesquilinear bracket, giving $\mathbb{R}e_0\oplus\mathfrak{su}(2)$; and the anti-Hermitian subspace, for the two brackets that reproduce the commutator up to sign, giving $\mathfrak{u}(2)$. The quaternion subspace is the one four-dimensional subspace carrying both a Jordan and a Lie algebra, the vector subspace and the anti-Hermitian subspace a Lie algebra alone, the Hermitian subspace a Jordan algebra alone, the centre both, of real dimension two, and the anti-quaternion subspace neither. The classification is *Remarkable Subspaces and the Four General Products*.

## Physical Readings

The four general products are the four jobs a relativistic quantum theory needs, and the four forms are the four quantities the jobs measure. The readings are the framework's naming of a proved algebra and are labelled as readings. **Composition**: the general plain bilinear product $\tilde P\tilde Q$ is the composition of two operations, associative, with the two-sided unit and the non-commutativity that reads as order, and its scalar part $\langle\cdot,\cdot\rangle$ is the **sector sign**, definite of signature $(0,4)$ on the material sector and $(4,0)$ on the informational one. **Probability**: the general plain sesquilinear product $\tilde P\tilde Q^{*}$ carries the positive definite form $\langle\cdot,\cdot\rangle_{*}$, the Born pairing of a state and an observable, and the unitary evolution built on it. **Causality**: the general quaternionic bilinear product $\tilde P^{\natural}\tilde Q$ squares to the interval, $\tilde Q^{\natural}\tilde Q=\langle\tilde Q\rangle_{\natural}e_0$, so that the mass shell is a level set of the multiplicative norm $\langle\cdot,\cdot\rangle_{\natural}$ and the light cone its zero set. **Gauge**: the general quaternionic sesquilinear product $\tilde P^{\natural}\tilde Q^{*}$ carries the indefinite Krein form $\langle\cdot,\cdot\rangle_{\natural*}$, real at the two equal arguments and unable to normalise a state, the form a gauge fixing uses rather than a probability.

Two statements bind the readings to the slots. The **second slot** divides the four into the two that can be iterated and the two that can only be evaluated: a composition and a causality may be composed, a probability and a gauge calibration may only be measured, and this is the algebra's own distinction between a dynamics and a pairing. The **first slot** divides the four into the two whose form is definite on each sector and the two whose form carries a signature: the sector sign $\langle\cdot,\cdot\rangle$ and the Born form $\langle\cdot,\cdot\rangle_{*}$ measure, the interval $\langle\cdot,\cdot\rangle_{\natural}$ and the Krein form $\langle\cdot,\cdot\rangle_{\natural*}$ carry a metric with a light cone. On the material sector $\mathbb{M}_-$ the four forms are real: the sector sign $\langle\cdot,\cdot\rangle$ is the negative of the Euclidean square, $\langle\cdot,\cdot\rangle_{*}$ is the Euclidean square, the interval $\langle\cdot,\cdot\rangle_{\natural}$ is the metric of signature $(3,1)$ and $\langle\cdot,\cdot\rangle_{\natural*}$ is its negative. The full reading of the four forms on the remarkable subspaces is *Remarkable Subspaces and the Four Forms*, and the four readings are collected in *The Four General Products and Their Physical Readings*.

## Summary

The biquaternion complex space carries four general products, the four insertions of a conjugation into a slot of one multiplication: the general plain bilinear $\tilde P\tilde Q$, the general plain sesquilinear $\tilde P\tilde Q^{*}$, the general quaternionic bilinear $\tilde P^{\natural}\tilde Q$ and the general quaternionic sesquilinear $\tilde P^{\natural}\tilde Q^{*}$. The two bilinear products are $\mathbb{C}$-bilinear and can be iterated, the two sesquilinear ones are conjugate-linear in the second slot and can only be evaluated; no two of the four agree on every pair, and exactly one, the general plain product, is associative.

The scalar part of each product is a degree-two form, and the four forms are one bilinear form $\langle\cdot,\cdot\rangle$ read through the two involutions, $H=\langle\tilde P,\tilde Q^{*}\rangle$, $N=\langle\tilde P^{\natural},\tilde Q\rangle$ and $K=\langle\tilde P^{\natural},\tilde Q^{*}\rangle$. Their algebraic norms are four, of which $\langle\cdot,\cdot\rangle_{*}$ is positive definite and $\langle\cdot,\cdot\rangle_{\natural}$ is multiplicative; $\langle\cdot,\cdot\rangle_{\natural}$ is the norm of no other product, and $\langle\cdot,\cdot\rangle_{*}$ is the only one definite on each remarkable subspace. The four general products preserve a remarkable subspace for exactly two subspaces, the centre and the quaternion subspace, and it is there, with the Hermitian subspace, that a Jordan or a Lie structure forms.

The four products are read physically as composition, probability, causality and gauge, and the four forms as the sector sign, the Born pairing, the interval and the Krein calibration; the second slot decides whether the job is a composition or a pairing, and the first slot whether its form measures or carries a metric. The products are the source of the band: the twelve products are the four together with their parts, and the twelve structures are the algebraic structures of those twelve operations.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra, basis $e_0,e_1,e_2,e_3$, central imaginary $i$ |
| $\tilde P=P_0e_0+\vec P$ | a biquaternion, its scalar part and vector part |
| ${}^{\natural}$, $\bar{\cdot}$, ${}^{*}$ | the natural, the coefficientwise and the Hermitian conjugation |
| $\tilde P\tilde Q$, $\tilde P\tilde Q^{*}$, $\tilde P^{\natural}\tilde Q$, $\tilde P^{\natural}\tilde Q^{*}$ | the four general products |
| $K_1(\tilde P)K_2(\tilde Q)$ | the general product as one multiplication with two inserted conjugations |
| $\langle\cdot,\cdot\rangle$, $\langle\cdot,\cdot\rangle_{*}$, $\langle\cdot,\cdot\rangle_{\natural}$, $\langle\cdot,\cdot\rangle_{\natural*}$ | the four forms: general plain bilinear, general plain sesquilinear, general quaternionic bilinear, general quaternionic sesquilinear |
| $\langle\tilde P^{\natural}\tilde Q\rangle_{\natural}=\langle\tilde P\rangle_{\natural}\langle\tilde Q\rangle_{\natural}$ | the multiplicativity of the quaternionic norm |
| $\langle\tilde Q\rangle_{*}=\sum_\mu\lvert Q_\mu\rvert^{2}$ | the positive definite Hermitian norm, the unique topological norm |
| $L^{\star}_{\tilde P}$, $R^{\star}_{\tilde P}$ | the left and right multiplication in a product, and $(L_{\tilde A})^{\dagger}=L_{\tilde A^{*}}$ |
| $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$, $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$, $\mathbb{M}_-$ | the six remarkable subspaces |

## Further Reading

- *The Four General Products of the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/the-four-general-products-of-the-biquaternioid-c-space.md`), for the four products in coordinates and their scalar–vector forms.
- *Relations Between the Four General Products* (`articles_maths/relations-between-the-four-general-products.md`), for the splitting identities, the conjugate of a product and the four scalar parts.
- *Comparison Between the Four General Products* (`articles_maths/comparison-between-the-four-general-products.md`), for the property table: associativity, the units and the commutativity of the four.
- *The Four General Products and Operators* (`articles_maths/the-four-general-products-and-operators.md`), for the division of labour between the product, the pairing and the inserted sign.
- *The 4 Forms over the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/the-4-forms-over-the-biquaternioid-c-space.md`) and *The 4 Algebraic Norms over the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/the-4-algebraic-norms-over-the-biquaternioid-c-space.md`), for the four forms, their count and their algebraic norms.
- *Remarkable Subspaces and the Four General Products* (`articles_maths/remarkable-subspaces-and-the-four-general-products.md`) and *Remarkable Subspaces and the Four Forms* (`articles_maths/remarkable-subspaces-and-the-four-forms.md`), for the four products and the four forms on the six subspaces.
- *Conventions in the Biquaternion Universe* (`articles_physics/conventions-in-the-biquaternion-universe.md`), for the conventions of the algebra, the conjugations and the remarkable subspaces.
- *The Four General Products and Their Physical Readings* (`articles_physics/the-four-general-products-and-their-physical-readings.md`), for the four physical readings of the four products and the four forms.
- Companion articles *The Twelve Products and the Twelve Algebraic Structures* (`articles_physics/the-twelve-products-and-the-twelve-algebraic-structures.md`) and *The Four Forms, the Four Algebraic Norms and the Change of Scalars* (`articles_physics/the-four-forms-the-four-algebraic-norms-and-the-change-of-scalars.md`).
