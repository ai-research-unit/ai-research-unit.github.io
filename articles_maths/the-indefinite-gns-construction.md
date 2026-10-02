# __The Indefinite GNS Construction__

## Introduction

The GNS construction turns a state on a $\ast$-algebra into a representation: from a positive linear functional $\omega$ one forms the sesquilinear form $\omega(y^{\dagger}x)$, divides by its radical and completes, obtaining a Hilbert space with a cyclic vector $\xi_{\omega}$ and a $\ast$-representation $\pi_{\omega}$ for which $\omega(x) = \langle\pi_{\omega}(x)\xi_{\omega},\xi_{\omega}\rangle$. Every axiom of the construction depends on the positivity of $\omega$: it is positivity that makes the form an inner product and the radical what it is.

The **indefinite GNS construction** drops positivity and keeps the rest. From a linear functional $\omega$ for which $\omega(x^{\dagger}x)$ is real but may be negative — an **indefinite state**, or a **weight** — the form $[x,y]_{\omega} = \omega(y^{\dagger}x)$ is Hermitian and invariant under the left multiplication, but it is indefinite, and the quotient of the algebra by its radical is a pre-Krein space rather than a pre-Hilbert one. Completing it in a majorant produces a **Krein space**, the left regular representation becomes a $\ast$-representation preserving the indefinite form, and $\omega$ is recovered as the diagonal matrix element $[\pi_{\omega}(x)\xi_{\omega},\xi_{\omega}]$.

What the construction adds beyond the positive case is a choice. The indefinite form has no norm, so the completion has to be taken in a **majorant** — a positive definite form with $|[x,y]_{\omega}| \leq c\,\|x\|\,\|y\|$ — and different majorants give different, though equivalent, Krein spaces with different fundamental symmetries $J$. So the datum of an indefinite GNS representation is the pair (indefinite state, majorant), and the positive definite inner product, the topology, and the $J$ of the resulting Krein space are exactly what the majorant supplies. This is the precise sense in which the fundamental symmetry selects the positive definite inner product, and it is the difference from the classical construction, where the positive form is the majorant and there is nothing to choose.

The Hilbert algebra and its positivity are *Hilbert Algebras*; the indefinite form, the fundamental symmetry and the Krein algebra are *Indefinite Inner Product Spaces*, *The Fundamental Symmetry* and *Krein Algebras*; the positive case of this construction is *The GNS Construction*; its representational use is *Krein–von Neumann Algebras* and *The Indefinite Modular Operator*. Those are cited. The base is $\mathbb{C}$-valued, the involution is $\dagger$, the indefinite form of the representation is $[\cdot,\cdot]$ and the induced majorant norm is $\|\cdot\|$.

## Indefinite States and the Form

**Definition.** A linear functional $\omega : A\to\mathbb{C}$ on a unital $\ast$-algebra is an **indefinite state** when

$$
\omega(x^{\dagger}) = \overline{\omega(x)}, \qquad \omega(x^{\dagger}x)\in\mathbb{R} \text{ for every } x,
$$

and it is a **state** when in addition $\omega(x^{\dagger}x)\geq0$ and $\omega(1) = 1$. The **form of $\omega$** is

$$
[x,y]_{\omega} = \omega(y^{\dagger}x).
$$

**Proposition (the form is Hermitian and invariant).** $[x,y]_{\omega}$ is Hermitian, $[x,y]_{\omega} = \overline{[y,x]_{\omega}}$, and it is invariant under the left regular representation:

$$
[xy,z]_{\omega} = [y,x^{\dagger}z]_{\omega} .
$$

**Proof.** The Hermitian symmetry is $\overline{\omega(y^{\dagger}x)} = \omega(x^{\dagger}y)$ by the reality condition; the invariance is $\omega(z^{\dagger}xy) = \omega((x^{\dagger}z)^{\dagger}y)$, the definition of the form on both sides.

**Definition.** The **radical** of the form is $N_{\omega} = \{x : [x,y]_{\omega} = 0 \text{ for every } y\} = \{x : \omega(y^{\dagger}x) = 0 \text{ for every } y\}$.

**Proposition.** $N_{\omega}$ is a left ideal, $\overline{N_{\omega}} = N_{\omega}$ for the positive states and the involution flips the two radicals: $N_{\omega}^{\dagger}$ is a right ideal. For a positive state the Cauchy–Schwarz inequality of an inner product holds and $N_{\omega} = \{x : \omega(x^{\dagger}x) = 0\}$.

**Proof.** The ideal property is the invariance of the form; the two descriptions of the radical for a positive state are the standard consequence of the Cauchy–Schwarz inequality; for an indefinite form the inequality fails and the two descriptions differ.

**Remark (the radical in the indefinite case).** For an indefinite state the set $\{x : \omega(x^{\dagger}x) = 0\}$ may be larger than the radical, because a form can be indefinite and yet vanish on a vector's diagonal without vanishing on the whole line; the quotient must be taken by the radical and not by the null set, and this is the first place where the construction differs from the positive one.

## The Construction

**Theorem (the indefinite GNS representation).** Let $\omega$ be an indefinite state on $A$ and suppose there is a positive definite form $\langle\cdot,\cdot\rangle$ on $A$ with

$$
|[x,y]_{\omega}| \leq c\,\|x\|\,\|y\|, \qquad \|x\|^{2} = \langle x,x\rangle ,
$$

for some constant $c$ (a **majorant** of $[\,,\,]_{\omega}$). Then the completion $K_{\omega}$ of $A/N_{\omega}$ in the norm induced by the majorant is a Krein space, the left regular representation descends to a $\ast$-representation

$$
\pi_{\omega} : A\to\mathcal{L}(K_{\omega}), \qquad \pi_{\omega}(x)(y + N_{\omega}) = xy + N_{\omega} ,
$$

which preserves the indefinite form, and the class $\xi_{\omega} = 1 + N_{\omega}$ is **cyclic** with

$$
[\pi_{\omega}(x)\xi_{\omega}, \xi_{\omega}] = \omega(x), \qquad [\pi_{\omega}(x)\xi_{\omega}, \pi_{\omega}(y)\xi_{\omega}] = \omega(y^{\dagger}x).
$$

**Proof.** The form descends to the quotient because the radical is exactly the set orthogonal to everything; it is Hermitian and invariant there; the majorant makes the quotient a pre-Hilbert space whose completion is a Krein space with the form extended by continuity, which is possible because the majorant bounds it; the left multiplication descends because $N_{\omega}$ is a left ideal, and the invariance of the form is the adjoint axiom for the representation. Cyclicity is the density of the image of $A$, and the two displayed identities are the definitions.

**Proposition (the model of the positive case).** If $\omega$ is a state then $\omega$ itself, $\langle x,y\rangle = \omega(y^{\dagger}x)$, is a majorant and the construction returns the classical GNS Hilbert space with its cyclic vector and representation.

**Proof.** Positivity of $\omega$ makes the form positive definite, so the majorant bound is trivial and the Krein space is a Hilbert space.

## The Difference from the Positive GNS

**Proposition (three differences).** The indefinite construction differs from the positive one in exactly three points:

- the **quotient**: it is taken by the radical of an indefinite form, which need not be the null set $\{x : \omega(x^{\dagger}x) = 0\}$;
- the **completion**: the indefinite form has no norm, so a majorant, hence an extra datum, is required, and the completion is a Krein space and not a Hilbert space;
- the **cyclic vector**: $\xi_{\omega}$ is cyclic but not of norm one, and $[\xi_{\omega},\xi_{\omega}] = \omega(1)$ may be negative or zero.

**Proof.** Each statement is the corresponding difference in the theorem; the vanishing of $[\xi_{\omega},\xi_{\omega}]$ happens when $\omega(1) = 0$, in which case the cyclic vector is neutral.

**Remark (what positivity did).** In the positive case the state supplies its own majorant, the radical is the null set, the completion is canonical and the cyclic vector may be normalised; every one of these conveniences is a consequence of the Cauchy–Schwarz inequality, which an indefinite state does not have. The indefinite construction is therefore not a weakening but a genuinely different construction, indexed by an extra choice.

## The Fundamental Symmetry and the Majorant

**Theorem (the role of $J$).** The fundamental symmetry of the Krein space $K_{\omega}$ produced by a majorant is exactly the operator attached to that majorant: if $\langle\cdot,\cdot\rangle$ is the majorant and $[\cdot,\cdot]$ the form, then $J$ is the unique operator with

$$
[x,y] = \langle Jx,y\rangle, \qquad J^{2} = \mathrm{id}, \qquad \langle Jx,y\rangle = \langle x,Jy\rangle ,
$$

and different majorants give Krein spaces with the same representation up to the equivalence of *The Fundamental Symmetry* and different operators $J$.

**Proof.** A majorant for an indefinite form on a Krein space is the form of a fundamental symmetry, by the bridge of *The Fundamental Symmetry*; the uniqueness is the uniqueness of that operator, and the equivalence is the equivalence of the induced forms.

**Corollary (the pair is the datum).** The indefinite GNS construction associates to a pair $(\omega, \text{majorant})$ a Krein-space representation; the indefinite state alone fixes the representation up to the choice of $J$, and the choice of $J$ fixes the topology.

**Proof.** The representation is defined on the quotient by $\omega$ alone, and the topology and the $J$ come from the majorant.

**Remark (the positive case as the canonical majorant).** A state distinguishes the majorant: the form itself. In the indefinite case no majorant is distinguished by $\omega$, and the extra choice is the price of dropping positivity; the choice is discussed again in *Krein–von Neumann Algebras*, where it becomes the choice of a $J$-representation.

## Worked Cases

### The Trivial Indefinite State

Let $A = \mathbb{C}^{2}$ with the pointwise product and the conjugation involution, and let $\omega(a,b) = a - b$. Then $\omega(x^{\dagger}x) = |x_{1}|^{2} - |x_{2}|^{2}$ is real and indefinite, $\omega(1,1) = 0$, and the form $[x,y]_{\omega} = x_{1}\bar y_{1} - x_{2}\bar y_{2}$ has trivial radical. The majorant $\langle x,y\rangle = x_{1}\bar y_{1} + x_{2}\bar y_{2}$ completes $A$ to the Krein space $\mathbb{C}^{1,1}$ and the fundamental symmetry is $\mathrm{diag}(1,-1)$.

### A Negative Weight

On the same algebra let $\omega(a,b) = -b$. Then $[x,y]_{\omega} = -x_{2}\bar y_{2}$ has radical $\{x : x_{2} = 0\}$, the quotient is one-dimensional, and the completed Krein space is $\mathbb{C}^{0,1}$ with $[\xi_{\omega},\xi_{\omega}] = \omega(1) = -1$.

### The Positive Case

For a state, say $\omega(a,b) = a$ on the same algebra, the construction yields the one-dimensional Hilbert space of the GNS representation of *The GNS Construction*, with $\xi_{\omega}$ of norm one; this is the boundary case in which the choice of majorant disappears.

## Summary

The **indefinite GNS construction** starts from an **indefinite state**, a linear functional $\omega$ with $\omega(x^{\dagger}x)$ real but not necessarily positive, and forms the Hermitian, left-invariant but indefinite form $[x,y]_{\omega} = \omega(y^{\dagger}x)$. Dividing the algebra by the **radical** of that form and completing in a **majorant** — a positive definite form that bounds it — produces a **Krein space** $K_{\omega}$ on which the left regular representation is a $\ast$-representation preserving the form, with a cyclic vector $\xi_{\omega}$ satisfying $[\pi_{\omega}(x)\xi_{\omega},\xi_{\omega}] = \omega(x)$ and $[\pi_{\omega}(x)\xi_{\omega},\pi_{\omega}(y)\xi_{\omega}] = \omega(y^{\dagger}x)$. It differs from the classical construction of *The GNS Construction* in three points: the quotient is by the radical of an indefinite form and not by the null set; the completion requires an extra datum, the majorant, and yields a Krein space; and the cyclic vector need not have norm one and may be neutral. The **fundamental symmetry** is the operator of the chosen majorant, $[x,y] = \langle Jx,y\rangle$, so the datum of the construction is the pair (indefinite state, majorant), the state fixing the representation up to $J$ and $J$ fixing the topology. The indefinite form and $J$ are *Krein Algebras* and *The Fundamental Symmetry*, the positive case is *The GNS Construction*, and the operator algebras are *Krein–von Neumann Algebras*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\omega$ | Indefinite state, $\omega(x^{\dagger}x)\in\mathbb{R}$ |
| $[x,y]_{\omega} = \omega(y^{\dagger}x)$ | The form of the state |
| $N_{\omega}$ | Radical of the form; the quotient is by it |
| $\langle\cdot,\cdot\rangle$, $c$ | Majorant and its bound $|[x,y]_{\omega}|\leq c\|x\|\|y\|$ |
| $K_{\omega}$ | The completed Krein space |
| $\pi_{\omega}$, $\xi_{\omega}$ | Representation and cyclic vector |
| $[\pi_{\omega}(x)\xi_{\omega},\xi_{\omega}] = \omega(x)$ | Recovery of the state |
| $J$, $[x,y] = \langle Jx,y\rangle$ | Fundamental symmetry attached to the majorant |

## Further Reading

- János Bognár, *Indefinite Inner Product Spaces*, Ergebnisse der Mathematik und ihrer Grenzgebiete 78 (Springer, 1974), for the completion of an indefinite form and the majorant.
- Konrad Schmüdgen, *Unbounded Operator Algebras and Representation Theory* (Akademie-Verlag, 1990), for representations of $\ast$-algebras with indefinite inner products.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. 1 (Academic Press, 1983), for the classical GNS construction against which the indefinite one is compared.
- Tomas Ya. Azizov and Iosif S. Iokhvidov, *Linear Operators in Spaces with an Indefinite Metric* (Wiley, 1989), for the majorants and the operators they define.
- Ola Bratteli and Derek W. Robinson, *Operator Algebras and Quantum Statistical Mechanics*, vol. 1 (Springer, 1987), for states, weights and the GNS representation.
