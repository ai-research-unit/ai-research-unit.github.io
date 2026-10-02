# __Krein–von Neumann Algebras__

## Introduction

A von Neumann algebra is a $\ast$-algebra of bounded operators on a Hilbert space closed in the weak operator topology; equivalently, by the bicommutant theorem, it is the commutant of its commutant. On a Krein space the same definition has to be read with the indefinite adjoint, and two questions arise at once: which algebras of operators deserve the name, and whether the bicommutant theorem survives. The answer is that the theorem survives for the algebras that respect the fundamental symmetry, and those are exactly the **Krein–von Neumann algebras**.

The adjoint for an indefinite form is not the Hilbert adjoint, and the equality $T^{\dagger} = J T^{*} J$ shows that the two differ by conjugation with $J$. An algebra of operators closed under the indefinite adjoint is therefore closed under $T\mapsto JT^{*}J$, and this is the whole content of the definition. The **$J$-representations** are the $\ast$-representations for which the representing operators are closed in this sense; the **$J$-commutant** is the set of bounded operators commuting with the algebra, and the **$J$-bicommutant theorem** says that a unital algebra closed under the indefinite adjoint and closed in the weak topology equals its own double commutant, exactly as in the definite case, provided the commutant is taken among the bounded operators of the Krein space.

The modular theory of the indefinite setting – the modular operator and the modular conjugation attached to a $J$-cyclic and $J$-separating vector – is the content of *The Indefinite Modular Operator* and *Krein–Tomita–Takesaki Theory*, and the analytic machinery of unbounded operators is flagged to *Analysis on Linear Spaces* (Part III). This article fixes the $J$-representations, the operator algebras on a Krein space, the $J$-commutant and the $J$-bicommutant theorem.

The indefinite form, the fundamental symmetry and the operator $J$ are *Indefinite Inner Product Spaces*, *The Fundamental Symmetry*, *J-Self-Adjoint and J-Unitary Operators*; the representation theory that produces these algebras is *The Indefinite GNS Construction*; the Hilbert-space case is *Von Neumann Algebras and the Hilbert Algebra Completeness* and *The Modular Operator and Tomita-Takesaki Theory*; the Krein algebras are *Krein Algebras*. Those are cited. The Krein space is $K$ with form $[\cdot,\cdot]$, definite form $\langle x,y\rangle = [Jx,y]$, and $T^{\dagger}$ is the adjoint for the indefinite form.

## $J$-Representations

**Definition.** A **$J$-representation** of a unital $\ast$-algebra $A$ on a Krein space $K$ is a linear map $\pi : A\to\mathcal{L}(K)$ with

$$
\pi(xy) = \pi(x)\pi(y), \qquad \pi(1) = \mathrm{id}, \qquad \pi(x^{\dagger}) = \pi(x)^{\dagger} ,
$$

where $T^{\dagger} = JT^{*}J$ is the adjoint for the indefinite form. A **non-degenerate** $J$-representation is one with $\overline{\pi(A)\xi} = K$ for every $\xi\neq0$, equivalently $\overline{\pi(A)K} = K$.

**Proposition (the adjoint in terms of $J$).** For a bounded operator $T$ on $K$ the indefinite adjoint exists, is unique and equals $T^{\dagger} = JT^{*}J$, where $T^{*}$ is the adjoint for the definite form; and $T\mapsto T^{\dagger}$ is an involutive antiautomorphism of $\mathcal{L}(K)$ that reverses products, $(TS)^{\dagger} = S^{\dagger}T^{\dagger}$.

**Proof.** The defining relation $[Tx,y] = [x,T^{\dagger}y]$ reads $\langle JTx,y\rangle = \langle Jx,T^{\dagger}y\rangle = \langle x, J T^{\dagger}y\rangle$, so the operator $JT^{\dagger}$ is the definite adjoint of $JT$, that is $JT^{\dagger} = (JT)^{*} = T^{*}J$, giving $T^{\dagger} = JT^{*}J$; uniqueness is the non-degeneracy of the form.

**Proposition (the $J$-representation as a definite one).** A map $\pi$ is a $J$-representation of $A$ on $K$ if and only if it is an algebra representation of $A$ on the Hilbert space $(K,\langle\cdot,\cdot\rangle)$, $\pi(xy) = \pi(x)\pi(y)$ and $\pi(1) = \mathrm{id}$, which is $\ast$-preserving in the **twisted** sense $\pi(x^{\dagger}) = J\pi(x)^{*}J$. In particular a $J$-representation is determined by its values and its $J$, and for $J = \mathrm{id}$ it is an ordinary $\ast$-representation.

**Proof.** Substitute the formula of the previous proposition into the third axiom of the definition.

**Proposition (self-adjoint elements of the representation).** An element $x = x^{\dagger}$ has $\pi(x)$ self-adjoint for the indefinite form, and then $J\pi(x)$ is self-adjoint for the definite form; conversely $\pi(x)$ self-adjoint for the indefinite form forces $x = x^{\dagger}$ when $\pi$ is faithful.

**Proof.** $T^{\dagger} = JT^{*}J$ gives $T^{\dagger} = T$ if and only if $JT$ is definite-self-adjoint; the converse is faithfulness.

## Operator Algebras on Krein Spaces

**Definition.** A **$J$-algebra** is a subalgebra $\mathcal{M}\subseteq\mathcal{L}(K)$ that is unital, closed under the indefinite adjoint $T\mapsto T^{\dagger}$, and closed in the weak operator topology. A **Krein–von Neumann algebra** is a $J$-algebra.

**Proposition (the definite translation).** $\mathcal{M}$ is a $J$-algebra if and only if it is a unital subalgebra of $\mathcal{L}(K)$ closed in the weak operator topology and satisfying

$$
J\mathcal{M}^{*}J = \mathcal{M}, \qquad \mathcal{M}^{*} = \{\,T^{*} : T\in\mathcal{M}\,\} .
$$

If in addition $J\in\mathcal{M}$ then $\mathcal{M}$ is a von Neumann algebra of the Hilbert space $(K,\langle\cdot,\cdot\rangle)$ containing $J$; conversely every such von Neumann algebra is a $J$-algebra.

**Proof.** The first statement is the identity $T^{\dagger} = JT^{*}J$ read as a set identity, weak closure being preserved because $J$ is bounded with bounded inverse. For the second, if $T\in\mathcal{M}$ and $J\in\mathcal{M}$ then $T^{*} = JT^{\dagger}J$ lies in $\mathcal{M}$, because $T^{\dagger}\in\mathcal{M}$ and $\mathcal{M}$ is an algebra containing $J$; so $\mathcal{M}$ is $\ast$-closed, that is a von Neumann algebra of the Hilbert space. The converse is the same identity.

**Definition.** The **$J$-commutant** of a set $\mathcal{S}\subseteq\mathcal{L}(K)$ is

$$
\mathcal{S}^{c} = \{\, T\in\mathcal{L}(K) : TS = ST \text{ for every } S\in\mathcal{S} \,\},
$$

the ordinary commutant; the **$J$-bicommutant** is $\mathcal{S}^{cc}$. When $\mathcal{S}$ is $J$-closed, so is every commutant of it and every bicommutant, as the next proposition shows.

**Proposition (the commutant is a $J$-algebra).** If $\mathcal{S}$ is $J$-closed then $\mathcal{S}^{c}$ is a $J$-algebra, and $\mathcal{S}\subseteq\mathcal{S}^{cc}$.

**Proof.** The commutant of a $J$-closed set is closed under the indefinite adjoint: if $T$ commutes with all $S$ then $T^{\dagger}$ does, because $TS = ST$ implies $S^{\dagger}T^{\dagger} = T^{\dagger}S^{\dagger}$ and $S^{\dagger}$ ranges over $\mathcal{S}$; weak closure and the algebra properties are those of a commutant.

## The $J$-Bicommutant Theorem

**Theorem ($J$-bicommutant).** Let $\mathcal{M}$ be a unital $J$-algebra on a Krein space $K$ containing the identity and the fundamental symmetry $J$. Then

$$
\mathcal{M}^{cc} = \mathcal{M} .
$$

Equivalently, a unital algebra of bounded operators closed under the indefinite adjoint and in the weak operator topology is a Krein–von Neumann algebra.

**Proof.** The hypothesis $J\in\mathcal{M}$ makes $\mathcal{M}$ a von Neumann algebra of the Hilbert space $(K,\langle\cdot,\cdot\rangle)$, by the definite translation; the commutant of $\mathcal{M}$ is defined by products alone, so the definite and the ordinary commutant of $\mathcal{M}$ are the same set. The classical bicommutant theorem for Hilbert-space von Neumann algebras therefore gives $\mathcal{M}^{cc} = \mathcal{M}$.

**Corollary (which algebras contain $J$).** A Krein–von Neumann algebra that contains $J$ is exactly a von Neumann algebra of the Hilbert space $(K,\langle\cdot,\cdot\rangle)$ containing $J$; equivalently, a Krein–von Neumann algebra that is not one of these does **not** contain $J$. Every Krein–von Neumann algebra containing $J$ is the commutant of its commutant, as in the definite theory.

**Proof.** If $J\in\mathcal{M}$ then $\mathcal{M}$ is $\ast$-closed by the definite translation, hence a Hilbert-space von Neumann algebra; conversely a Hilbert-space von Neumann algebra containing $J$ is closed under $T\mapsto JT^{*}J = T^{\dagger}$. The remaining assertion is the bicommutant theorem.

**Remark (why the hypothesis $J\in\mathcal{M}$ is not innocuous).** Without it there are $J$-algebras that are not von Neumann algebras of the Hilbert space, and for those the commutant does not see the indefinite adjoint. In $\mathbb{C}^{1,1}$ with $J = \mathrm{diag}(1,-1)$ take $\mathcal{M} = \mathrm{span}\{\mathrm{id}, T\}$ with $T = \left(\begin{smallmatrix}1&1\\-1&0\end{smallmatrix}\right)$: one has $T^{\dagger} = T$, so $\mathcal{M}$ is a $J$-algebra, but $T^{*} = \left(\begin{smallmatrix}1&-1\\1&0\end{smallmatrix}\right)$ is not in $\mathcal{M}$, so $\mathcal{M}$ is not $\ast$-closed, and $J\notin\mathcal{M}$. The commutant of $\mathcal{M}$ is the algebra of polynomials in $T$, which is again $\mathcal{M}$, so the bicommutant statement still holds there; what fails without $J\in\mathcal{M}$ is the reduction to the definite theory, and that is why the Krein–von Neumann algebras of the bicommutant theorem are required to contain $J$.

## Worked Cases

### The Trivial Algebras

For $\mathcal{M} = \mathcal{L}(K)$ the commutant is the scalars, and the bicommutant is again the scalars' commutant, $\mathcal{L}(K)$: the theorem is the classical double-commutant statement. For $\mathcal{M}$ the algebra generated by $J$ alone, the commutant is the set of operators preserving both eigenspaces of $J$, and the bicommutant returns the algebra of $J$.

### A Pontryagin Space

Let $K = \mathbb{C}^{1,1}$ with $J = \mathrm{diag}(1,-1)$ and $\mathcal{M}$ the diagonal $2\times2$ matrices. Then $\mathcal{M}$ is a $J$-algebra containing $J$, its commutant is the diagonal matrices themselves, and $\mathcal{M}^{cc} = \mathcal{M}$: the operators preserving the two indefinite directions form a Krein–von Neumann algebra of indefinite dimension two.

### The Definite Case

For a Hilbert space, $J = \mathrm{id}$ and every von Neumann algebra is a Krein–von Neumann algebra; the $J$-bicommutant theorem is then the classical one, and the theorem is a strict extension of it.

## Summary

On a Krein space the adjoint for the indefinite form is $T^{\dagger} = JT^{*}J$, and a **$J$-representation** of a $\ast$-algebra is a representation satisfying $\pi(x^{\dagger}) = JT^{*}J$-adjoint, equivalently a Hilbert-space $\ast$-representation whose operators are $J$-twisted. A **$J$-algebra**, or **Krein–von Neumann algebra**, is a unital algebra of bounded operators closed under $T\mapsto T^{\dagger}$ and in the weak operator topology; these are exactly the algebras with $J\mathcal{M}^{*}J = \mathcal{M}$, and those of them that contain $J$ are exactly the von Neumann algebras of the Hilbert space containing $J$. The **$J$-commutant** is the ordinary commutant, it is a $J$-algebra when the algebra is, and the **$J$-bicommutant theorem** holds: a unital $J$-algebra containing $J$ equals its double commutant, so the theory is the Hilbert-space theory conjugated by $J$. The hypothesis that $J$ belongs to the algebra is what reduces the statement to the classical one: it forces $\mathcal{M}$ to be $\ast$-closed, that is a von Neumann algebra of the underlying Hilbert space, and it is not automatic, since there are algebras with $J\mathcal{M}^{*}J = \mathcal{M}$ that are not $\ast$-closed. The representation theory that produces these algebras is *The Indefinite GNS Construction*, the modular theory is *The Indefinite Modular Operator* and *Krein–Tomita–Takesaki Theory* with the analytic machinery deferred to *Analysis on Linear Spaces* (Part III), and the definite case is *The Modular Operator and Tomita-Takesaki Theory* and *Von Neumann Algebras and the Hilbert Algebra Completeness*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $T^{\dagger} = JT^{*}J$ | Adjoint for the indefinite form |
| $\pi$, $\pi(x^{\dagger}) = \pi(x)^{\dagger}$ | $J$-representation |
| $\mathcal{L}(K)$ | Bounded operators on the Krein space |
| $\mathcal{M}$, $J$-algebra | Krein–von Neumann algebra |
| $\mathcal{S}^{c}$, $\mathcal{S}^{cc}$ | $J$-commutant and $J$-bicommutant |
| $T\mapsto JT$ | Definite translation, a von Neumann algebra containing $J$ |
| $\mathcal{M}^{cc} = \mathcal{M}$ | The $J$-bicommutant theorem |
| $J\in\mathcal{M}$ | The indispensable hypothesis |

## Further Reading

- János Bognár, *Indefinite Inner Product Spaces*, Ergebnisse der Mathematik und ihrer Grenzgebiete 78 (Springer, 1974), for the operators of a Krein space and their adjoints.
- Tomas Ya. Azizov and Iosif S. Iokhvidov, *Linear Operators in Spaces with an Indefinite Metric* (Wiley, 1989), for the algebras of operators preserving an indefinite form.
- Konrad Schmüdgen, *Unbounded Operator Algebras and Representation Theory* (Akademie-Verlag, 1990), for representations of $\ast$-algebras with indefinite adjoints.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. 1 (Academic Press, 1983), for the classical bicommutant theorem against which the $J$-version is read.
- Ola Bratteli and Derek W. Robinson, *Operator Algebras and Quantum Statistical Mechanics*, vol. 1 (Springer, 1987), for von Neumann algebras and their commutants.
