
# __The Graded Action on a Module over a Topological Vector Space__

## Introduction

A topological algebra graded by a continuous involutive automorphism, $E = E_{0} \oplus E_{1}$, acts on a **graded module** $M = M_{0} \oplus M_{1}$ when the action respects the two gradings, $E_{i}M_{j} \subseteq M_{i+j}$: the even elements of $E$ preserve the two parts of the module and the odd elements exchange them. Such an action is the module-level form of the sign carried by the signed operators, and the compatibility is exactly the statement that the action operators commute with the two grade involutions up to the parity sign. This article defines the graded topological module, states the compatibility in its equivalent forms, records the canonical example in which the module is the algebra itself, and names the sign rule of the graded tensor product without using it.

The grading of the algebra, the grade involution and the parity are *The Signed Sandwich on a Topological Vector Space* and *Reflections as Signed Two-Sided Operators on a Topological Vector Space*; the signed operators, of which the graded action is the module-level counterpart, are *The Signed Sandwich on a Topological Vector Space* and *The Signed Left Multiplication on a Topological Vector Space*; the module structure of the algebra over itself is *The Left and Right Multiplication Operators on a Topological Vector Space*; the abstract version is *The Graded Action on a Module over an Algebra* in the next category of this Part. The sign rule of the graded tensor product and the general theory of graded modules over graded algebras are owned by the graded-algebra category and are named here, not used. No form and no element involution is used.

Throughout, $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$, $E = E_{0} \oplus E_{1}$ is a graded unital topological algebra over $\mathbb{K}$ with a jointly continuous multiplication and its grade involution $\alpha$, $+1$ on $E_{0}$ and $-1$ on $E_{1}$, and $M = M_{0} \oplus M_{1}$ is a Hausdorff topological vector space over $\mathbb{K}$ with a continuous action $E \times M \to M$ making it a topological left $E$-module, together with its **grade involution** $\beta$, $+1$ on $M_{0}$ and $-1$ on $M_{1}$. The action of $x \in E$ on $M$ is written $\rho_{x}$.

## Graded Modules and the Compatible Action

**Definition.** The action of $E$ on $M$ is **compatible** with the gradings when

$$
E_{i}\,M_{j} \subseteq M_{i+j} \qquad (i, j \in \{0, 1\}) ,
$$

that is, when the even operators preserve the two parts of $M$ and the odd operators exchange them. A module with a compatible action is a **graded module** over the graded algebra $E$.

**Proposition (the equivalent form).** The action is compatible if and only if for every homogeneous $x \in E_{i}$ and every $m \in M$,

$$
x\,\beta(m) = (-1)^{i}\,\beta(x\,m),
$$

equivalently $\beta(xm) = (-1)^{i}x\beta(m)$; the two grade involutions therefore satisfy $\beta\rho_{x} = (-1)^{i}\rho_{x}\beta$ on the homogeneous part $E_{i}$.

**Proof.** If $m \in M_{j}$ and $x \in E_{i}$ then $xm \in M_{i+j}$, so $\beta(xm) = (-1)^{i+j}xm = (-1)^{i}x((-1)^{j}m) = (-1)^{i}x\beta(m)$; conversely this identity for all homogeneous $m$ forces $x(M_{j}) \subseteq M_{i+j}$, since for $m \in M_{j}$ it gives $\beta(xm) = (-1)^{i+j}xm$, which says that $xm$ lies in the $(-1)^{i+j}$-eigenspace of $\beta$, namely $M_{i+j}$.

**Proposition (continuity).** The grade involutions $\alpha$ and $\beta$ are continuous, the projections onto the graded parts $M_{j}$ are continuous, and the action restricts to continuous maps $E_{i} \times M_{j} \to M_{i+j}$.

**Proof.** The projections onto the graded parts are the idempotents $(1 \pm \beta)/2$, continuous because $\beta$ is; the restriction of a continuous action to a product of closed subspaces is continuous, and the graded parts are closed because they are the kernels of $\mathrm{id} \mp \beta$.

## The Canonical Example and the Module Endomorphisms

**Proposition (the algebra as its own graded module).** $M = E$ with the grading $E = E_{0} \oplus E_{1}$, the grade involution $\beta = \alpha$, and the action $\rho_{x}(y) = xy$ is a graded left $E$-module; the inclusions $E_{i}E_{j} \subseteq E_{i+j}$ hold because an even element preserves the two parts and an odd one exchanges them.

**Proof.** The action is associative and unital by the definition of the multiplication, and the inclusions are the parity statement of the grading; the module axioms are those of the left regular module of *The Left and Right Multiplication Operators on a Topological Vector Space*.

**Proposition (the induced involution on the module endomorphisms).** The algebra $\operatorname{End}_{E}(M)$ of continuous module endomorphisms is graded by

$$
\operatorname{End}_{E}(M)_{i} = \{f : f(M_{j}) \subseteq M_{i+j}\},
$$

with grade involution $\gamma(f) = \beta f \beta$, and the same holds for the algebra $\mathcal{L}(M)$ of all continuous endomorphisms of $M$.

**Proof.** Composition of endomorphisms adds parities, since $f(M_{j}) \subseteq M_{i+j}$ and $g(M_{k}) \subseteq M_{l+k}$ give $gf(M_{j}) \subseteq M_{i+l+j}$; conjugation by the involutive automorphism $\beta$ is an order-two automorphism with the two eigenspaces given by the two inclusions $f(M_{j}) \subseteq M_{j}$ and $f(M_{j}) \subseteq M_{1-j}$, so it is the grade involution.

**Proposition (the canonical graded module of operators).** For a topological vector space $F = F_{0} \oplus F_{1}$ graded by a continuous involution $T$, the algebra $\mathcal{L}(F)$ is graded, the space $F$ is a graded $\mathcal{L}(F)$-module with $\beta = T$ acting by evaluation, and the compatibility is the statement that an operator of parity $i$ maps the part $F_{j}$ into $F_{i+j}$.

**Proof.** The action of $\mathcal{L}(F)$ on $F$ is evaluation, $(\rho_{A})(v) = Av$; compatibility is the definition of the grading of $\mathcal{L}(F)$, and the parity statement is the proposition above specialised to $M = F$.

## The Deferred Sign Rule

**Remark (no sign in the compatibility).** The compatibility above carries no sign: the grade involutions commute or anticommute on the homogeneous parts, and no sign enters the action itself. The sign rule that makes the tensor product of two graded modules a graded module with the twisted flip belongs to the graded-algebra category, where it is owned together with the general theory of graded modules over graded algebras; it is named here because the graded actions of the later articles refer to it, and it is neither defined nor used.

## Examples

**Example (the operator algebra of a graded space).** Let $F = F_{0} \oplus F_{1}$ with a continuous involution $T$ and let $E = \mathcal{L}(F)$ with $\alpha(A) = TAT$. Then $M = F$ with $\beta = T$ is a graded $E$-module: an even operator preserves $F_{0}$ and $F_{1}$, an odd one exchanges them, and the compatibility identity $\beta(Av) = (-1)^{i}A\beta(v)$ holds on the homogeneous part $E_{i}$.

**Example (the algebra as a module over itself).** For $M = E$ with $\beta = \alpha$ the action is the multiplication, the even part $E_{0}$ acts on the two parts of $E$, the odd part $E_{1}$ exchanges them, and the module endomorphisms are the right multiplications by elements intertwining the gradings.

**Example (the commutative case).** On $E = C(K)$ with $\alpha(f) = f \circ \sigma$, a graded module is a pair of topological vector spaces $M_{0}, M_{1}$ with the action of an even function preserving them and an odd function exchanging them; the compatibility identity is the parity statement, and no sign enters because the base algebra is commutative.

## Summary

A graded topological algebra $E = E_{0} \oplus E_{1}$ with grade involution $\alpha$ acts on a graded topological module $M = M_{0} \oplus M_{1}$ with grade involution $\beta$ compatibly when $E_{i}M_{j} \subseteq M_{i+j}$, equivalently when the action operators satisfy the sign relation $\beta\rho_{x} = (-1)^{i}\rho_{x}\beta$ on the homogeneous part $E_{i}$; then the even operators preserve the two parts of $M$ and the odd ones exchange them, and the action is determined by its two even and two odd restrictions. The grade involutions and the graded projections are continuous, so the restrictions of the action to the graded pieces are continuous. The canonical example is the algebra itself with the left regular action and $\beta = \alpha$; the module endomorphisms form a graded algebra with grade involution $\gamma(f) = \beta f \beta$, and the evaluation of the operator algebra of a graded topological vector space is the canonical graded module of operators. The compatibility carries no sign; the sign rule of the graded tensor product belongs to the graded-algebra category of this Part and is named, not used. The adjoint version of the graded action is *The Graded Adjoint Action on a Module over a Topological Vector Space*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $E = E_{0} \oplus E_{1}$ | Graded topological algebra |
| $\alpha$ | Grade involution, $+1$ on $E_{0}$, $-1$ on $E_{1}$ |
| $M = M_{0} \oplus M_{1}$ | Graded topological module |
| $\beta$ | Grade involution of $M$ |
| $E_{i}M_{j} \subseteq M_{i+j}$ | Compatibility of the action with the gradings |
| $\beta\rho_{x} = (-1)^{i}\rho_{x}\beta$ | Equivalent form, $x \in E_{i}$ |
| $\operatorname{End}_{E}(M)_{i}$ | Graded module endomorphisms |
| $\gamma(f) = \beta f\beta$ | Grade involution on the endomorphisms |
| evaluation | The graded module $F$ over $\mathcal{L}(F)$ |

## Further Reading

- Nicolas Bourbaki, *Algebra I* (Springer, 1989), for graded modules over graded algebras and the sign rule of the graded tensor product.
- Charles E. Rickart, *General Theory of Banach Algebras* (Van Nostrand, 1960), for the graded algebras and their involutions.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras I* (Academic Press, 1983), for the graded modules and the graded operators.
- Helmut H. Schaefer and Manfred P. Wolff, *Topological Vector Spaces* (Springer, second edition, 1999), for the topological modules and their continuous actions.
- John B. Conway, *A Course in Functional Analysis* (Springer, second edition, 1990), for the module structure of the operator algebra and its gradings.
