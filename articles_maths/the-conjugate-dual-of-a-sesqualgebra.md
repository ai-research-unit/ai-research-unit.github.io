# __The Conjugate Dual of a Sesqualgebra__

## Introduction

*Conjugate-Linear Maps and the Conjugate Dual* defines the conjugate dual of an $R$-module as the module of $\varsigma$-semilinear maps into $R$, proves that it is the ordinary dual of the conjugate module, and reads the evaluation as a pairing that is linear in the first slot and $\varsigma$-semilinear in the second. This article adds the topology: the base is an involutive topological ring, the sesqualgebra is an object of *Topological Sesqualgebras*, the conjugate module carries the topology of the object, and the conjugate dual is the module of the **continuous** semilinear functionals. It is the topological counterpart of the Part I entry, and it is the receiver of the second slot for the whole topological layer.

The one new ingredient with respect to Part I is continuity. The conjugate dual of the article is a submodule of the algebraic conjugate dual, namely the intersection of the semilinear functionals with the continuous ones, and over a topological module of the layer it is the object that carries the weak topology of the second slot. Because a continuous semilinear functional is a continuous linear functional of the conjugate module, the topological two-readings theorem is an isomorphism of topological modules, and it is the map that lets the sesquilinear product and the sesquilinear forms of the layer be received. In the normed case the conjugate dual is a Banach space with the operator norm, which is the trace norm in the finite-dimensional matrix case by the duality of the operator and the trace class.

Three facts organise the article. The conjugate dual $A^{\varsigma*}$ of a sesqualgebra is the ordinary dual of the conjugate module $A^{\varsigma}$ as a topological module and, in the normed case, as a Banach space; this is the topological form of the two-readings theorem of Part I, and it is the reason no separate theory of "continuous semilinear functionals" has to be built. The evaluation $(f,x)\mapsto f(x)$ is continuous on $A^{\varsigma*}\times A^{\varsigma}$ for the dual topology and the topology of the object, and the ordinary dual cannot supply the second slot, because a continuous linear functional is linear in every variable and cannot produce the conjugated scalar that a sesquilinear product requires. And the transpose of a continuous semilinear map flips the two duals, $f^{*} : B^{*} \to A^{\varsigma*}$ and $f^{*} : B^{\varsigma*} \to A^{*}$, continuously for the dual topologies; the evaluation $\mathrm{ev} : A \to (A^{\varsigma*})^{*}$ is $\varsigma$-semilinear and is the ordinary evaluation of the conjugate module, so reflexivity is inherited from the conjugate module.

The article defines the topology on the conjugate module and the conjugate dual, proves the two-readings and the transpose theorems topologically, reads the pairings and the evaluation, treats reflexivity and its failure, and reads the field, the matrix, the sequence and the function examples. It cites the analytic prerequisites rather than proving them: the dual of a normed or Banach space and its weak topologies are *Normed and Banach Spaces*, §*The Dual Space* and *The Dual Operator and the Weak Topology*, the completion of the dual is not used, and the algebraic statements are *Conjugate-Linear Maps and the Conjugate Dual*. Throughout, $(R,\varsigma)$ is a commutative involutive topological ring with $\varsigma$ continuous, $A$ is a topological sesqualgebra over $(R,\varsigma)$, and the conjugate module $A^{\varsigma}$ carries the topology of $A$ declared in *Topological Sesqualgebras*, §*The Conjugate Module*. When a norm is used, $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$, $\varsigma$ its continuous involution, and $A$ is a normed sesqualgebra in the sense of *Banach Sesqualgebras*.

## The Topology on the Conjugate Module

### The Conjugate Module and Its Topology

**Proposition (the conjugate module is the module).** Let $A$ be a topological sesqualgebra over $(R,\varsigma)$ and let $A^{\varsigma}$ be its conjugate module, the module $A$ with the action $\lambda \cdot x = \varsigma(\lambda)x$. Then $A^{\varsigma}$ is a topological $R$-module for the topology of $A$, the identity $A \to A^{\varsigma}$ is a homeomorphism of the additive topological groups, and it is an isomorphism of topological $R$-modules exactly when $\varsigma = \mathrm{id}$.

*Proof.* The twisted action is continuous because $\varsigma$ is continuous and the scalar action of $A$ is continuous, this being the content of *Topological Sesqualgebras*, §*The Conjugate Module*; the additive group and its topology are those of $A$, so the identity is a homeomorphism. The action is the ordinary action exactly when $\varsigma = \mathrm{id}$. $\square$

**Remark.** The two modules share one topology, one fundamental system of neighbourhoods of $0$ and one uniformity, so they share the compact subsets and the bounded subsets; this is why the dual topologies of the next section need not be defined twice.

### The Continuous Semilinear Functionals

**Definition.** Let $A$ be a topological sesqualgebra over $(R,\varsigma)$. A **continuous $\varsigma$-semilinear functional** on $A$ is an additive map $f : A \to R$ with $f(\lambda x) = \varsigma(\lambda)f(x)$ that is continuous for the topology of $A$ and the topology of $R$. The set of them is written

$$
A^{\varsigma*} = \operatorname{Hom}^{\mathrm{cts}}_{\varsigma}(A, R) .
$$

It is an $R$-submodule of the algebraic conjugate dual $\operatorname{Hom}_{\varsigma}(A,R)$ of *Conjugate-Linear Maps and the Conjugate Dual*, §*Definition*, with the pointwise action, and it contains the ordinary continuous dual $A^{*} = \operatorname{Hom}^{\mathrm{cts}}_{R}(A,R)$ exactly when $\varsigma = \mathrm{id}$.

**Proposition (the submodule).** $A^{\varsigma*}$ is an $R$-module under pointwise addition and the pointwise action $(\lambda f)(x) = \lambda f(x)$, it is a submodule of $\operatorname{Hom}_{\varsigma}(A,R)$, and $\varsigma = \mathrm{id}$ gives $A^{\varsigma*} = A^{*}$.

*Proof.* The sum of two additive semilinear maps is additive and semilinear, and the pointwise multiple $\lambda f$ satisfies $(\lambda f)(\mu x) = \lambda\varsigma(\mu)f(x) = \varsigma(\mu)(\lambda f)(x)$, so it is semilinear; the sum and the multiple of continuous maps are continuous. The statements about $\varsigma = \mathrm{id}$ are the collapse of the scalar rules. $\square$

## The Conjugate Dual

### Definition

**Definition.** The **conjugate dual** of $A$ is the $R$-module $A^{\varsigma*}$ of continuous semilinear functionals, equipped with the topology of uniform convergence on the compact subsets of $A$; in the normed case, where $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$ and $A$ is a normed sesqualgebra over $(\mathbb{K},\varsigma)$, it carries the operator norm

$$
\lVert f\rVert = \sup\{\lvert f(x)\rvert : x \in A, \ \lVert x\rVert \leq 1\}.
$$

**Remark (the conjugate dual is not the conjugate module).** The conjugate module $A^{\varsigma}$ is the module with the scalars twisted and the conjugate dual $A^{\varsigma*}$ is a module of maps into $R$; the two carry different symbols, as in *Conjugate-Linear Maps and the Conjugate Dual*, §*Definition*, and the conjugate dual of $A$ is the ordinary dual of $A^{\varsigma}$.

### The Two Readings

**Theorem (the topological two-readings).** Let $A$ be a topological sesqualgebra over $(R,\varsigma)$. Then the identity on underlying sets is an isomorphism of topological $R$-modules

$$
A^{\varsigma*} \;\cong\; (A^{\varsigma})^{*},
$$

the ordinary continuous dual of the conjugate module, and it maps the topology of uniform convergence on the compact subsets to itself. In the normed case the isomorphism is an isometry of Banach spaces, and likewise $(A^{\varsigma})^{\varsigma*} \cong A^{*}$.

*Proof.* A semilinear $f : A \to R$ is a linear $f : A^{\varsigma} \to R$ by the two-readings theorem of *Conjugate-Linear Maps and the Conjugate Dual*, §*The Two Readings by Linear Maps*, and the reading changes nothing but the action declared on the source, so it preserves continuity; conversely a continuous linear functional of $A^{\varsigma}$ is a continuous semilinear functional of $A$. The compact subsets are the same in the two modules, by the remark of §*The Conjugate Module and Its Topology*, so the topologies of compact convergence correspond. In the normed case the two operator norms are computed over the same unit ball, because $A$ and $A^{\varsigma}$ have the same norm and the scalar rule of a semilinear functional reads $\lvert f(\lambda\cdot x)\rvert = \lvert\varsigma(\lambda)\rvert\lvert f(x)\rvert = \lvert\lambda\rvert\lvert f(x)\rvert$, so the identification is isometric; the second isomorphism applies the first to $A^{\varsigma}$ and uses $(A^{\varsigma})^{\varsigma} = A$. $\square$

**Corollary (the normed conjugate dual is a Banach space).** Let $A$ be a normed sesqualgebra over $(\mathbb{K},\varsigma)$. Then $A^{\varsigma*}$ with the operator norm is a Banach space over $\mathbb{K}$, and it is reflexive exactly when the conjugate module $A^{\varsigma}$ is.

*Proof.* The dual of a normed space is a Banach space, by *Normed and Banach Spaces*, §*The Dual Space*, and $A^{\varsigma*}$ is that dual by the theorem. A Banach space is reflexive exactly when its dual is, by the same section, and $A^{\varsigma*}$ is the dual of $A^{\varsigma}$. $\square$

### The Topology of the Dual

**Proposition (the weak-* topology).** The topology of pointwise convergence on $A^{\varsigma*}$ is the coarsest making every evaluation $f \mapsto f(x)$, $x \in A$, continuous; it is weaker than the topology of compact convergence, which is weaker than the operator norm topology in the normed case. The closed unit ball of $A^{\varsigma*}$ is weak-* compact when $A$ is a normed space, by the Banach–Alaoglu theorem.

*Proof.* The pointwise topology is generated by the evaluations and the compact-convergence topology contains it because a point is compact and convergence on compacta implies pointwise convergence; the norm topology contains the compact-convergence topology because a compact subset of a normed space is bounded and uniform convergence on bounded sets is stronger than on compacta. Banach–Alaoglu is *Normed and Banach Spaces*, §*The Dual Space*. $\square$

## The Pairing

### The Evaluation Pairing

**Theorem (the two pairings, continuous).** The evaluation $(f,x) \mapsto f(x)$ is a continuous $R$-bilinear pairing

$$
\langle \cdot, \cdot \rangle : A^{\varsigma*} \times A^{\varsigma} \longrightarrow R ,
$$

equivalently a pairing $A^{\varsigma*} \times A \to R$ that is $R$-linear in the first variable and $\varsigma$-semilinear in the second, on $A^{\varsigma*} \times A$. In the normed case the pairing satisfies $\lvert\langle f,x\rangle\rvert \leq \lVert f\rVert\lVert x\rVert$.

*Proof.* The bilinearity and the semilinearity are the theorem of *Conjugate-Linear Maps and the Conjugate Dual*, §*The Pairing*, and they are algebraic. Continuity holds because a continuous functional is a continuous map $A \to R$ and because the topology of the dual is a topology of convergence; in the normed case it is the defining property of the operator norm, $\lvert f(x)\rvert \leq \lVert f\rVert\lVert x\rVert$ for every $x$, with $\lVert x\rVert \leq 1$ giving the bound on the unit ball and homogeneity giving the general case. $\square$

**Proposition (the pairing separates the two modules).** Let $A$ be a locally convex Hausdorff space over the valued field $\mathbb{K}$ and let $\varsigma$ be the identity or the conjugation, so that it is continuous. If $f(x) = 0$ for every $x \in A$ then $f = 0$; and if $f(x) = 0$ for every $f \in A^{\varsigma*}$ then $x = 0$. So the evaluation pairing of the conjugate dual with the sesqualgebra is non-degenerate on both sides.

*Proof.* The first statement is the definition of a functional. For the second, let $x \neq 0$; by the Hahn–Banach theorem for a locally convex Hausdorff space there is a continuous linear functional $\ell$ with $\ell(x) \neq 0$, *Locally Convex Spaces*, §*Completeness and the Hahn–Banach Theorem*. Then $f = \varsigma \circ \ell$ is continuous and semilinear, $f(\lambda y) = \varsigma(\ell(\lambda y)) = \varsigma(\lambda)\varsigma(\ell(y)) = \varsigma(\lambda) f(y)$, and $f(x) = \varsigma(\ell(x)) \neq 0$. Hence the conjugate dual separates the points of $A$. $\square$

**Remark (what the pairing does not characterise).** The evaluation is not the only continuous bilinear pairing of $A^{\varsigma*}$ with $A$, since a scalar multiple is another, so it is canonical but is not singled out by a two-variable universal property. What is canonical is the identification of $A^{\varsigma*}$ with the dual of the conjugate module, and that identification is the pairing of Part I read with the two topologies.

### Why the Ordinary Dual Does Not See the Second Slot

**Remark (the obstruction).** A continuous linear functional of $A$ is linear in every variable it meets, so every pairing built from $A^{*}$ is linear in both slots and none can produce the conjugated scalar that the sesquilinear product requires in its second slot. The conjugate dual is exactly the receiver of that second slot, as in *Conjugate-Linear Maps and the Conjugate Dual*, §*The Pairing*, and the topological layer adds only that the receiving functional must be continuous. This is the reason the sesquilinear product $A \times A \to A$ is read on the pair $(A,A^{\varsigma})$ and not on a single dual, and it is why the weak topologies of the layer are the pairings of $A$ with $A^{\varsigma*}$.

### The Transpose

**Theorem (the transpose flips the two duals).** Let $f : A \to B$ be a continuous $\varsigma$-semilinear map of topological sesqualgebras over $(R,\varsigma)$. Then the pullback $g \mapsto g \circ f$ is a continuous linear map

$$
f^{*} : B^{*} \longrightarrow A^{\varsigma*}, \qquad f^{*} : B^{\varsigma*} \longrightarrow A^{*},
$$

and the two assignments are the same rule on the two duals.

*Proof.* This is the theorem of *Conjugate-Linear Maps and the Conjugate Dual*, §*The Transpose of a Conjugate-Linear Map*, which gives the parities: a linear $g$ composed with a semilinear $f$ is semilinear, and a semilinear $g$ composed with a semilinear $f$ is linear. Continuity is the continuity of a composite of continuous maps, the dual topologies being topologies of convergence, and in the normed case it gives $\lVert f^{*}\rVert \leq \lVert f\rVert$ for the operator norms. $\square$

**Remark.** The transpose cannot stay on one dual, because composing with a semilinear map flips the parity; this is the dual form of the parity flip of *The Sesquilinear Product*, §*The Transposed Product*, and it is the reason the adjoint of a conjugate-linear operator is a different construction from the adjoint of a linear one.

## The Double Conjugate and Reflexivity

### The Evaluation

**Theorem (the evaluation is the evaluation of the conjugate module).** The canonical map

$$
\mathrm{ev} : A \longrightarrow (A^{\varsigma*})^{*}, \qquad \mathrm{ev}_{x}(f) = f(x),
$$

is $\varsigma$-semilinear and continuous; under the identification $(A^{\varsigma*})^{*} \cong (A^{\varsigma})^{**}$ it is the ordinary evaluation of the conjugate module. In the normed case $\mathrm{ev}$ is an isometry.

*Proof.* The semilinearity is the computation of *Conjugate-Linear Maps and the Conjugate Dual*, §*The Double Conjugate Dual and the Evaluation*: $\mathrm{ev}_{\lambda x}(f) = f(\lambda x) = \varsigma(\lambda)f(x) = \varsigma(\lambda)\mathrm{ev}_{x}(f)$. Continuity holds because $f$ is continuous and the dual topology is a topology of convergence; the identification of the double dual is the two-readings theorem applied twice, $(A^{\varsigma*})^{*} \cong ((A^{\varsigma})^{*})^{*} = (A^{\varsigma})^{**}$, and $\mathrm{ev}$ becomes the ordinary evaluation of $A^{\varsigma}$ under it. In the normed case the ordinary evaluation is an isometry by *Normed and Banach Spaces*, §*The Dual Space*, and the identification is isometric by the two-readings theorem. $\square$

### Reflexivity and Its Failure

**Definition.** The sesqualgebra $A$ is **reflexive** when the evaluation $\mathrm{ev} : A \to (A^{\varsigma*})^{*}$ is an isomorphism of topological modules; in the normed case, when it is an isometric isomorphism.

**Theorem (reflexivity is inherited).** Let $A$ be a topological sesqualgebra over $(R,\varsigma)$. Then $A$ is reflexive exactly when the conjugate module $A^{\varsigma}$ is reflexive in the ordinary sense.

*Proof.* By the theorem of §*The Evaluation*, $\mathrm{ev}$ is the ordinary evaluation of $A^{\varsigma}$ under the identification of the double duals, and the identification is an isomorphism of topological modules; so the two maps are the same map of the same pair of modules, and $A$ is reflexive exactly when $A^{\varsigma}$ is. $\square$

**Theorem (the failure of reflexivity).** Let $A = c_0$ with the supremum norm, the conjugation of the scalars and the termwise product $(x \star y)_k = x_k\bar y_k$. Then $A$ is a normed sesqualgebra over $(\mathbb{C},\varsigma)$, neither associative nor commutative, which is not reflexive; its conjugate dual is $A^{\varsigma*} \cong \ell^{1}$, and $(A^{\varsigma*})^{*} \cong \ell^{\infty} \neq c_0$.

*Proof.* The product is submultiplicative, $\lvert x_k\bar y_k\rvert \leq \lVert x\rVert_\infty\lVert y\rVert_\infty$ for every $k$, so $A$ is a normed sesqualgebra. The conjugate module $A^{\varsigma}$ is $c_0$ with the twisted action, which is the same Banach space, and $c_0^{*} \cong \ell^{1}$ with $(c_0)^{**} \cong \ell^{\infty}$, by *Normed and Banach Spaces*, §*The Dual Space*; since $c_0 \neq \ell^{\infty}$ the evaluation is not surjective. The conjugate dual is $\ell^{1}$ and the ordinary dual of $\ell^{1}$ is $\ell^{\infty}$ by the two-readings theorem, so reflexivity fails at the same place as it does for the Banach space. $\square$

**Remark.** The example is the reason the article separates the two duals: the sesquilinear structure is invisible to the failure of reflexivity, which is a property of the underlying Banach space and is inherited from the conjugate module. A sesqualgebra is reflexive exactly when its Banach space is, and the examples of reflexive objects are the reflexive Banach spaces, the Hilbert spaces and the $\ell^{p}$ with $1 < p < \infty$, read with any sesquilinear product that makes them sesqualgebras.

## Examples

### The Field and the Matrices

**Example (the field, verdict: the conjugate dual is the field).** Let $A = \mathbb{C}$ with the modulus, $\varsigma$ the conjugation and the product $z \star w = z\bar w$. A continuous semilinear functional is $f(z) = \lambda\bar z$ for a unique $\lambda \in \mathbb{C}$, and $\lVert f\rVert = \lvert\lambda\rvert$, so $A^{\varsigma*} \cong \mathbb{C}$ isometrically under $f \leftrightarrow \lambda$; the pairing is $\langle\lambda, z\rangle = \lambda\bar z$. The object is reflexive. It is the smallest instance of the two-readings theorem: the conjugate module of $\mathbb{C}$ is $\mathbb{C}$ itself, and the conjugate dual is its ordinary dual $\mathbb{C}$ with the semilinear reading.

**Example (the complex matrices, verdict: the conjugate dual is the trace class).** Let $A = M_n(\mathbb{C})$ with the operator norm, the conjugation and the product $S \star T = ST^{*}$. A continuous semilinear functional is $T \mapsto \mathrm{tr}(T^{*}C)$ for a unique $C \in M_n(\mathbb{C})$, and its operator norm is the trace norm $\lVert C\rVert_{1} = \mathrm{tr}\lvert C\rvert$, by the duality of the operator norm and the trace class; so $A^{\varsigma*} \cong M_n(\mathbb{C})$ isometrically under $C \mapsto \mathrm{tr}((\cdot)^{*}C)$, with the pairing $\langle C, T\rangle = \mathrm{tr}(T^{*}C)$. The object is reflexive, being finite-dimensional, and the identification is the matrix form of the Riesz representation of the Hilbert–Schmidt pairing.

### The Sequences and the Functions

**Example ($c_0$ and $\ell^{1}$, verdict: the failure of reflexivity).** The object $A = c_0$ of §*Reflexivity and Its Failure* has $A^{\varsigma*} \cong \ell^{1}$ and $(A^{\varsigma*})^{*} \cong \ell^{\infty}$; the evaluation $c_0 \to \ell^{\infty}$ is the inclusion and is not surjective. The example is the normed witness that reflexivity is a hypothesis and not a theorem of the layer.

**Example (the functions, verdict: the conjugate dual of a function algebra).** Let $X$ be compact Hausdorff and let $A = C(X,\mathbb{C})$ with the supremum norm, the conjugation of the scalars and the product $f \star g = f\bar g$. A continuous semilinear functional is $f \mapsto \int \bar f\,\mathrm{d}\mu$ for a complex measure $\mu$; by the Riesz representation theorem, $A^{*}$ is the space of complex measures, and the conjugate dual is the same space with the semilinear reading, so $A^{\varsigma*} \cong M(X)$ as a Banach space isometrically. The object is the infinite-dimensional model, and the integral that defines the functionals is Part III's, the representation theorem being quoted here.

## Summary

The **conjugate dual** of a topological sesqualgebra $A$ over $(R,\varsigma)$ is the $R$-module $A^{\varsigma*} = \operatorname{Hom}^{\mathrm{cts}}_{\varsigma}(A,R)$ of continuous semilinear functionals, carrying the topology of uniform convergence on the compact subsets of $A$ and, in the normed case, the operator norm $\lVert f\rVert = \sup\{\lvert f(x)\rvert : \lVert x\rVert \leq 1\}$. The **topological two-readings theorem** identifies $A^{\varsigma*}$ with the ordinary continuous dual of the conjugate module, $(A^{\varsigma})^{*}$, as a topological module and, in the normed case, isometrically; consequentially the normed conjugate dual is a Banach space, reflexive exactly when the conjugate module is. The **evaluation pairing** $\langle f,x\rangle = f(x)$ is continuous on $A^{\varsigma*} \times A^{\varsigma}$ and is the universal continuous pairing of the first slot of the dual with the second slot of the sesqualgebra, linear in the first slot and $\varsigma$-semilinear in the second; the **ordinary dual cannot see the second slot**, because a continuous linear functional is linear in every variable and cannot produce the conjugated scalar that a sesquilinear product requires. The **transpose** of a continuous semilinear map flips the two duals, $f^{*} : B^{*} \to A^{\varsigma*}$ and $f^{*} : B^{\varsigma*} \to A^{*}$, continuously. The **evaluation** $\mathrm{ev} : A \to (A^{\varsigma*})^{*}$ is $\varsigma$-semilinear and is the ordinary evaluation of the conjugate module, so **reflexivity is inherited**; the field $\mathbb{C}$, the matrices $M_n(\mathbb{C})$ with the trace norm, the reflexive Banach spaces and the function algebras are reflexive, while $c_0$ is not, its conjugate dual being $\ell^{1}$ and its double conjugate dual $\ell^{\infty}$. The construction is the topological form of *Conjugate-Linear Maps and the Conjugate Dual*, and its algebraic content is that article's; the topology adds the continuity of the functionals, of the pairing and of the transpose.

## Summary of Notation

| symbol | meaning |
|---|---|
| $(R,\varsigma)$ | a commutative involutive topological ring with $\varsigma$ continuous |
| $A^{\varsigma}$ | the conjugate module: the same topological module with the twisted action |
| $A^{*}$ | the ordinary continuous dual, $\operatorname{Hom}^{\mathrm{cts}}_{R}(A,R)$ |
| $A^{\varsigma*}$ | the conjugate dual, $\operatorname{Hom}^{\mathrm{cts}}_{\varsigma}(A,R)$ |
| $A^{\varsigma*} \cong (A^{\varsigma})^{*}$ | the topological two-readings theorem |
| $\langle f,x\rangle = f(x)$ | the continuous evaluation pairing, $\varsigma$-semilinear in the second slot |
| $f^{*} : B^{*} \to A^{\varsigma*}$, $f^{*} : B^{\varsigma*} \to A^{*}$ | the transpose of a continuous semilinear map flips the duals |
| $\mathrm{ev} : A \to (A^{\varsigma*})^{*}$ | the evaluation, the ordinary evaluation of $A^{\varsigma}$ |
| reflexive | $\mathrm{ev}$ is an isomorphism; inherited from the conjugate module |
| $\lVert C\rVert_{1} = \mathrm{tr}\lvert C\rvert$ | the trace norm, the operator norm on the conjugate dual of $M_n(\mathbb{C})$ |
| $\varsigma = \mathrm{id}$ | the collapse: $A^{\varsigma*} = A^{*}$ |

## Further Reading

- John B. Conway, *A Course in Functional Analysis* (Springer, second edition, 1990), for the dual of a normed space, the bidual, reflexivity and the weak and weak-* topologies.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume I* (Academic Press, 1983), for the duality of the operator norm with the trace class that the matrix example uses.
- Walter Rudin, *Real and Complex Analysis* (McGraw–Hill, third edition, 1987), for the Riesz representation theorem and the dual of the function algebras.
- Nelson Dunford and Jacob T. Schwartz, *Linear Operators, Part I* (Interscience, 1958), for the topology of compact convergence on a dual and its relation to the strong topology.
- Maria Fragoulopoulou, *Topological Algebras with Involution* (North-Holland, 2005), for the continuous semilinear functionals of an involutive topological algebra and their role in the duality of the layer.
- Harald Upmeier, *Jordan Algebras in Analysis, Operator Theory, and Quantum Mechanics* (American Mathematical Society, 1987), for the duality of the ternary product and the sesquilinear adjoint structures.
