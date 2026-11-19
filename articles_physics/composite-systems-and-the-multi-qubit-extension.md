# __Composite Systems and the Multi-Qubit Extension: The Module Route and the Algebra Route__

## Introduction

A one-qubit formalism has to answer one question before it can be extended: **what is the object that composes?** Two answers are available. An element composes as an element, and two systems are then one element of a larger algebra. A module composes as a module, and two systems are then one element of a tensor product of modules. The two answers are not the same, and the difference is not a matter of taste: they give the same state space and the same observables, and they differ on exactly one object.

**The claim of this article.** The corpus composes modules, not elements. That route is correct and not a compromise. The other route, which the notation sometimes suggests, would require a per-subsystem sector label, and that label is the one thing composition destroys. So the extension to $n$ qubits is not a new algebra: it is the tensor power of the defining module, together with an analysis of what happens to the material/informational split on the way.

**What composition destroys, and what it hands back.** The label is lost, and something is gained in its place. The alternating form of the one-qubit space tensors without obstruction, and its tensor square evaluated on a two-qubit state is twice the determinant of the coefficient array, whose modulus is the concurrence. The measure of entanglement of the pair is therefore a one-qubit canonical form applied to both factors, and the identity is exact. It is proved in [The Duo-Complex Bridge: The Three Canonical Forms and Their Tensor Powers](the-duo-complex-bridge-the-three-canonical-forms-and-their-tensor-powers.html)..

**Why the distinction has to be stated first.** Read quickly, the corpus appears to say that two qubits are two copies of $\mathbb{B}$, since a qubit is an element of $\mathbb{B}_{\Psi}$ and two qubits should be two such elements. That reading is wrong, and it is wrong in a way that produces false expectations: it predicts four sector labels, it predicts a four-dimensional state space for the pair, and it predicts a product on each corner. None of the three survives. This article separates the two routes, states what each one gives, and locates the single point at which they part.

**The sections.** *Two senses of composition* separates the element sense from the module sense. *The element route and its count* records why the element sense closes at one system. *The module route* states the construction the corpus uses. *The algebra route* states what the other construction would require, and shows that over $\mathbb{R}$ it exists. *Where the routes agree* proves that the observables coincide. *What only the algebra route would add* isolates the label and the central bit. *What the module route keeps and loses* is the balance sheet. *Names* fixes what the phrase *multi-qubit extension* is allowed to mean here.

The article uses [The Relativistic Qubit in Biquaternionic Form](the-relativistic-qubit-in-biquaternionic-form.html) for the module as the carrier of one qubit, [The Multi-Qubit Boundary](beyond-one-qubit-what-b-tensor-b-would-require.html) for the dimension count, [The Material-Informational Split as a Superselection Structure in Biquaternionic Form](the-material-informational-split-as-a-superselection-structure-in-biquaternionic-form.html) for the sectors, and [The Spinor Module in Biquaternionic Form and Its Lorentz Action](the-spinor-module-in-biquaternionic-form-and-its-lorentz-action.html) for the tensor powers. The two theorems that decide the question are proved in [The Multi-Qubit Split, I: The Antilinear Obstruction and the Corner Collapse](the-multi-qubit-split-i-the-antilinear-obstruction-and-the-corner-collapse.html); this article uses them and refers forward to them.

## Two Senses of Composition

**An element composes only if the algebra does.** In the element sense a state is a single element of $\mathbb{B}$: the informational state is $\tilde{Ϛ}_\Psi=\tfrac12(e_t+i\vec s_\Psi)$ with $\vec s_\Psi\in\mathbb{R}^3$ and $\lvert\vec s_\Psi\rvert\le 1$, and its data are the four real coordinates of a Hermitian element subject to one normalisation. To compose two such states in the same sense one needs a single element of a single algebra that carries both, which means an algebra into which $\mathbb{B}$ sits twice, compatibly with everything the states use: the product, the star, and the trace.

**A module composes without the algebra composing.** In the module sense a state is a ray of $S=\mathbb{C}^2$, the simple left module of $\mathbb{B}$. Two systems then have state space $S\otimes S=\mathbb{C}^4$, and the observables are the endomorphisms of that space. The algebra of the joint system is $\operatorname{End}(S\otimes S)=M_4(\mathbb{C})$, which is **not** a copy of $\mathbb{B}$ and does not need to be: the state never was an element of the algebra, and the Born rule reads it through the module.

**The two senses are one sense at $n=1$ and part company at $n=2$.** At one system they coincide because $\operatorname{End}(S)=\mathbb{B}$: the endomorphism algebra of the defining module is the algebra itself. That coincidence is the whole source of the confusion. It invites the inference that the endomorphism algebra of $S\otimes S$ is $\mathbb{B}\otimes\mathbb{B}$, which is true, and then that $\mathbb{B}\otimes\mathbb{B}$ is again a biquaternion algebra, which is false.

| | element route | module route |
| --- | --- | --- |
| what a state is | one element of $\mathbb{B}_{\Psi}$ | one ray of $S=\mathbb{C}^2$ |
| what composition is | an element of $\mathbb{B}\otimes\mathbb{B}$ | a ray of $S\otimes S$ |
| joint algebra | $\mathbb{B}\otimes_\mathbb{C}\mathbb{B}\cong M_4(\mathbb{C})$ | $\operatorname{End}(S\otimes S)\cong M_4(\mathbb{C})$ |
| what survives at $n=2$ | $M_4(\mathbb{C})$ | $M_4(\mathbb{C})$ |
| what does not survive | the element reading of the state | nothing |

**The table is the article in one glance.** The joint algebra is the same object in both columns. What differs is what each column promised about it: the element route promised that the state would remain an element, and it does not.

## The Element Route and Its Count

**One system, three parameters.** A state of one qubit is a positive Hermitian element of trace one, and the four dimensions of $\mathbb{B}_{\Psi}$ carry three after the trace constraint. The Bloch ball is that count, geometrically.

**Two systems, fifteen.** A state of two qubits is a positive element of $M_4(\mathbb{C})$ of trace one, whose real dimension is $16-1=15$. The counting is in [The Multi-Qubit Boundary](beyond-one-qubit-what-b-tensor-b-would-require.html), and it is worth repeating because it is the shortest argument in the corpus: **an element of $\mathbb{B}$ has four real parameters, and no element of anything of dimension four can carry fifteen.**

**The count is not the only obstruction, and this article adds nothing to it.** The dimension count, the absence of a degree-two algebra closed under composition, and the absence of a four-dimensional subspace holding the positive cone are the three supports of the verdict in that article. What is added here is a reading of the verdict: the failure belongs to the element route and not to the framework, because the framework never used the element route for composite systems.

**One system as an element and one system as a module are the same data.** The Hermitian element $\tilde{Ϛ}_\Psi=\tfrac12(e_t+i\vec s_\Psi)$ acts on $S$ as the density operator $\rho=\tfrac12(\mathrm I+\vec s_\Psi\cdot\boldsymbol\sigma)$, and every Hermitian element of $\mathbb{B}$ arises this way. So the element route is not an error at $n=1$; it is a presentation of the module data that happens to be available at one system. It stops being available at two.

## The Module Route

**The construction.** Take the defining module $S=\mathbb{C}^2$. The $n$-qubit state space is the tensor power

$$
S^{\otimes n}=\mathbb{C}^{2}\otimes\cdots\otimes\mathbb{C}^{2}=\mathbb{C}^{2^{n}} ,
$$

of complex dimension $2^{n}$ and real dimension $2^{n+1}$. The observables are the Hermitian operators on it, and the Born weight of an observable $\tilde A\in\mathrm{Herm}(M_{2^{n}}(\mathbb{C}))$ in the pure state $\psi\in S^{\otimes n}$ is

$$
\langle\psi\rvert\tilde A\lvert\psi\rangle=\bigl(H^{\otimes n}\bigr)(\psi,\tilde A\psi),
$$

with $H$ the Hermitian form of $S$. The mixed states are the positive operators of trace one, of real dimension $4^{n}-1$.

**The joint algebra is a matrix algebra and nothing else.** Its dimension over $\mathbb{C}$ is $4^{n}$, its centre is $\mathbb{C}\mathrm I$, it is simple, and it has no proper two-sided ideal. At $n=1$ it is $M_2(\mathbb{C})\cong\mathbb{B}$; at $n=2$ it is $M_4(\mathbb{C})$; at $n=3$ it is $M_8(\mathbb{C})$. There is no $n\ge 2$ at which it is again a biquaternion algebra, because a biquaternion algebra is $M_2$ and $M_{2^n}$ has degree $2^n$.

**The module route is what the corpus actually does.** The higher-spin carriers are built as tensor powers of $S$, not as tensor powers of $\mathbb{B}$: the spin-$s$ carrier is $\operatorname{sym}^{2s}(S)$, and the four-vector is a tensor carrier of a different kind. The same construction, read at $n$ factors, gives the $n$-qubit space. Nothing in the corpus's treatment of composite systems departs from it, and the two-qubit computations in [The Bell Basis as the Idempotent Basis of $\mathbb{B}\otimes\mathbb{B}$](the-bell-basis-as-the-idempotent-basis-of-b-tensor-b.html) are computations in it.

**What the route does not supply is a name.** The route says what the state space is and what acts on it. It does not say what becomes of the material/informational split, because the split is a property of $\mathbb{B}$, and the route has replaced $\mathbb{B}$ by $M_{2^{n}}(\mathbb{C})$. That question is not answered by choosing a route; it is answered by computing, and the computation is the subject of the next two articles.

## The Algebra Route

**What the algebra route would require.** Three items, in increasing strength.

1. A joint algebra into which $\mathbb{B}$ maps $n$ times, so that each factor's elements have a meaning in the joint system.
2. A sector label on each factor: a family of commuting involutions $\sigma_1,\dots,\sigma_n$ of the joint algebra, with $\sigma_j$ acting as the star on the $j$-th factor and as the identity on the others, so that the four corners of a pair, or the $2^{n}$ corners of an $n$-tuple, are the joint eigenspaces.
3. A product respecting the labels, so that a corner is an algebra and not only a subspace.

**Over $\mathbb{R}$ the route exists.** Take the real tensor product $\mathbb{B}^{\otimes_{\mathbb{R}}n}$. Its complexification is $\bigl(\mathbb{H}^{\otimes n}\bigr)\otimes_{\mathbb{R}}\mathbb{C}\cong M_{2^{n}}(\mathbb{C})$, because $\mathbb{H}^{\otimes n}$ is a central simple real algebra of degree $2^{n}$ and the complexification of such an algebra is a full matrix algebra. Hence

$$
\mathbb{B}^{\otimes_{\mathbb{R}}n}\;\cong\;\bigl(\mathbb{C}^{\otimes_{\mathbb{R}}n}\bigr)\otimes_{\mathbb{R}}M_{2^{n}}(\mathbb{C})\;\cong\;\bigoplus_{k=1}^{2^{n-1}}M_{2^{n}}(\mathbb{C}),
$$

of real dimension $2^{3n}$, which is $64$ at $n=2$ and $512$ at $n=3$. The involutions $\sigma_j$ are well defined here, because $\mathbb{B}^{\otimes_{\mathbb{R}}n}$ has not been quotiented: the two imaginary units of two different factors remain distinct, and the star of one factor acts on an object that still remembers which factor it came from.

**The labels are real-linear and they exist, so item 2 is not vacuous.** This is the point that makes the algebra route worth stating rather than dismissing. Over $\mathbb{R}$ one can label each factor informational or material, and the $2^{n}$ labels are genuine joint eigenspaces. What one cannot do is carry them through the quotient that turns the real tensor product into the complex one.

**Over $\mathbb{C}$ the route dies, and it dies at item 2.** The complex tensor product is the quotient of $\mathbb{B}^{\otimes_{\mathbb{R}}n}$ by the relations that identify the central units of the factors: $i\otimes e_t=e_t\otimes i$ for a pair, and the corresponding relations for $n$ factors. The partial star does not respect those relations, so it does not descend, and there is no label. The proof is two lines and is given in [The Multi-Qubit Split, I](the-multi-qubit-split-i-the-antilinear-obstruction-and-the-corner-collapse.html); the content of the two lines is that $\sigma_j$ reverses the sign of the central scalar while the relation that defines the quotient is a statement about that scalar.

**So the algebra route is a route over $\mathbb{R}$ and not over $\mathbb{C}$.** A reader who wants it must take the real tensor product, accept an algebra of twice the size, and accept the central bit that comes with it. That is exactly what [The Multi-Qubit Split, II](the-multi-qubit-split-ii-the-sign-condition-the-concurrence-form-and-the-central-bit.html) constructs, and it is the reason the central bit appears there rather than being invented.

## Where the Routes Agree

**The observables coincide, and this is a theorem.** Over $\mathbb{C}$, take the real span of the decomposable tensors all of whose factors lie in $\mathbb{B}_{\Psi}$. Since the tensors of $\mathbb{B}_{\Psi}$ alone include every product of the four elements $e_t,i\vec e_x,i\vec e_y,i\vec e_z$, there are $4^{n}$ of them, and their real span is exactly

$$
\operatorname{span}_{\mathbb{R}}\bigl\{a_1\otimes\cdots\otimes a_n\;:\;a_j\in\mathbb{B}_{\Psi}\bigr\}=\mathrm{Herm}\bigl(M_{2^{n}}(\mathbb{C})\bigr),
$$

of real dimension $4^{n}$, which is the whole Hermitian part. The same holds for the anticorner with an odd number of material factors, whose span is the anti-Hermitian part. Both statements are proved in [The Multi-Qubit Split, I](the-multi-qubit-split-i-the-antilinear-obstruction-and-the-corner-collapse.html).

**What this says in words.** The observables of the joint system are generated by the informational observables of the factors, with no remainder. So the module route's observable space and the algebra route's observable space are the same space, reached from two directions. The difference between the routes is therefore not in what can be measured. It is in whether a measurement can be *labelled* as informational on one factor and material on another.

**The Born rule coincides for the same reason.** The weight $\langle\psi\rvert\tilde A\lvert\psi\rangle$ is $\bigl(H^{\otimes n}\bigr)(\psi,\tilde A\psi)$, and $H^{\otimes n}$ is the tensor power of a form on $\mathbb{B}_{\Psi}$'s module. The rule is stated in the module's language in both routes; the element route supplies an element only at $n=1$, where the two languages coincide.

**The agreement is exact and it is not an accident of dimension.** It follows from $\mathrm{Herm}(M_{2^{n}})=\operatorname{span}_{\mathbb{R}}\bigl(\mathrm{Herm}(M_2)^{\otimes n}\bigr)$, which holds because the Hermitian part of a tensor product of matrix algebras is spanned by Hermitian tensors of Hermitian factors. A reader who has seen the dimension count $4^{n}=4^{n}$ may take this for granted; it is a statement about the *product*, not only about the count, and the proof uses the corner identity.

## What Only the Algebra Route Would Add, and What It Costs

**The label.** With a family of sector labels one could ask of a joint observable whether it is informational on the first factor and material on the second, and the answer would be a definite sign pattern. Without the labels that question has no content: the observable is a Hermitian element of $M_4(\mathbb{C})$, and every Hermitian element is a real combination of informational times informational tensors, so the sign pattern is not merely unknown but undefined.

**The central bit.** The real tensor product carries a central involution $\mathsf J=i\otimes i$ and, with it, two central idempotents. Passing from $\mathbb{R}$ to $\mathbb{C}$ discards the involution as a structure and keeps only its value, $-1$. So the algebra route buys the labels and pays with an extra central bit that the complex quotient freezes. Both objects are computed in [The Multi-Qubit Split, II](the-multi-qubit-split-ii-the-sign-condition-the-concurrence-form-and-the-central-bit.html).

**The cost is not small, and it is not a cost in physics.** Doubling the algebra doubles the parameter count of every operator, and the extra parameters are not observable: they are the two summands, of which one is selected. Nothing in the framework selects it. The corpus is therefore right to compose over $\mathbb{C}$ and to record the real algebra as an analysis rather than a construction.

## What the Module Route Keeps and What It Loses

**It keeps the states, the observables, the weights, the dynamics and the entanglement measures.** Every computation stays correct, at every $n$. The concurrence, the reductions, the Bell basis, the teleportation protocol and the entropy are all computations in the module route, and they do not change.

**It loses the element reading of a state and the per-factor sector label.** At $n=1$ a state can be read as an element of the algebra; at $n\ge2$ it cannot, because the element would have to live in a four-dimensional slice that does not hold the cone. The per-factor label goes for the reason of the previous sections. Both losses are exact statements and neither is a defect of the framework: they are properties of the tensor product.

**It gains one thing that the element route would hide.** Refusing the quotient, and looking at what the real algebra has that the complex one does not, is what produces the parity rule of [The Multi-Qubit Split, I](the-multi-qubit-split-i-the-antilinear-obstruction-and-the-corner-collapse.html) and the central bit of [The Multi-Qubit Split, II](the-multi-qubit-split-ii-the-sign-condition-the-concurrence-form-and-the-central-bit.html). That is a statement about the split, obtained by taking the element route seriously enough to see where it goes. The module route alone would never have asked.

## Names

**The phrase *multi-qubit extension* names two different projects and this article separates them.** The first project is a new algebra whose elements are multi-qubit states. It does not exist and cannot exist, by the dimension count. The second is the tensor power of the defining module, together with the analysis of what the framework's own structures do under that tensor power. It exists, it is what the corpus uses, and it is what the rest of this group of articles is about.

**So the extension is not a replacement for the tensor product.** It is the tensor product, read through the corpus's objects. The three canonical forms of the duo-complex space tensor to the three structures of the $n$-qubit theory, which is [The Duo-Complex Bridge](the-duo-complex-bridge-the-three-canonical-forms-and-their-tensor-powers.html), and the split is analysed in the two articles before it. Nothing in the group proposes a different state space.

**One consequence of the naming, stated so it is not expected.** There is no $n$-qubit state that is a single biquaternion, at any $n\ge2$. A biquaternion holds one qubit, and a pair holds four complex amplitudes, which is two biquaternions' worth of data with a different product. The disparity is not a gap to be filled; it is the content of the dimension count.

## What Is Not Claimed

**No physics changes.** The framework's predictions at one system are untouched, and at $n$ systems the predictions were already those of the tensor product. What changes is the description of how the framework's two sectors behave under composition.

**The module route is not a retreat.** It is stated here as the correct construction, not as the lesser of two evils. The corpus has used it since the higher-spin articles, and the two-sector literature has never needed anything else.

**The algebra route is not refuted in general.** It exists over $\mathbb{R}$, it carries the labels, and it carries the central bit. What is refuted is the claim that it can be had over $\mathbb{C}$ with the labels intact.

**No identification of the central bit with a physical charge is asserted.** The bit is an algebraic object. Whether anything in nature reads it is not decided here and is not decided anywhere in the corpus.

## Summary

A qubit is the defining module $S=\mathbb{C}^2$ of $\mathbb{B}\cong M_2(\mathbb{C})$, and the endomorphism algebra of $S$ is $\mathbb{B}$ itself, which is why the element reading works at one system. Two qubits are $S\otimes S=\mathbb{C}^4$ with endomorphism algebra $M_4(\mathbb{C})$. Read as elements, two qubits would need a four-dimensional state space and have fifteen, so the element reading stops. The algebra route — a joint algebra with a sector label per factor and a product respecting the labels — exists over $\mathbb{R}$, where $\mathbb{B}^{\otimes_{\mathbb{R}}n}\cong\bigoplus_{k=1}^{2^{n-1}}M_{2^{n}}(\mathbb{C})$ and the partial stars are well defined, and it fails over $\mathbb{C}$, where the quotient that identifies the central units kills them. The two routes agree exactly on the observables, because the real span of the informational tensors is the whole Hermitian part of $M_{2^{n}}(\mathbb{C})$. So composition costs the label and the element reading, and buys nothing observable; the central bit of the real algebra is the residue, and the module route keeps every computation.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}\cong M_2(\mathbb{C})$ | the biquaternion algebra, real dimension eight |
| $\mathbb{B}_{\Psi}$, $\mathbb{B}_{\Phi}$ | the informational and material sectors, the $\pm1$ eigenspaces of the star |
| $S=\mathbb{C}^2$ | the defining module, the carrier of one qubit |
| $S^{\otimes n}=\mathbb{C}^{2^{n}}$ | the $n$-qubit carrier |
| $M_{2^{n}}(\mathbb{C})$ | the joint algebra of $n$ qubits |
| $\mathbb{B}^{\otimes_{\mathbb{R}}n}$ | the real tensor product, of real dimension $2^{3n}$ |
| $\bigoplus_{k=1}^{2^{n-1}}M_{2^{n}}(\mathbb{C})$ | its complexification, the $2^{n-1}$ summands |
| $\sigma_j$ | the partial star on the $j$-th factor |
| $\tilde{Ϛ}_\Psi=\tfrac12(e_t+i\vec s_\Psi)$ | the one-qubit state as a positive Hermitian element |
| $4^{n}-1$ | the real dimension of the $n$-qubit state space |

## Further Reading

**In this category.** [The Relativistic Qubit in Biquaternionic Form](the-relativistic-qubit-in-biquaternionic-form.html) establishes the module as the carrier. [The Multi-Qubit Boundary](beyond-one-qubit-what-b-tensor-b-would-require.html) is the dimension count and the verdict. [The Material-Informational Split as a Superselection Structure in Biquaternionic Form](the-material-informational-split-as-a-superselection-structure-in-biquaternionic-form.html) fixes the two sectors. [The Multi-Qubit Split, I](the-multi-qubit-split-i-the-antilinear-obstruction-and-the-corner-collapse.html) proves the non-descent and the corner collapse. [The Multi-Qubit Split, II](the-multi-qubit-split-ii-the-sign-condition-the-concurrence-form-and-the-central-bit.html) proves the sign condition and constructs the central bit. [The Duo-Complex Bridge](the-duo-complex-bridge-the-three-canonical-forms-and-their-tensor-powers.html) states what survives composition. [Higher Spin from Tensor Products](higher-spin-from-tensor-products-the-three-carriers-and-the-absence-of-a-fourth.html) is the module route used for another purpose, and the clearest existing statement that the module and not the element is what composes.

**In the mathematics corpus.** [The Category of Modules in the Biquaternion Algebra](../articles_maths/the-category-of-modules.html) proves that $S$ is the unique simple left module and that every module is a direct sum of copies of it, which is the structural reason a module route exists at all.
