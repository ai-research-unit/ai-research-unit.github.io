# __The Superalgebra Reading and the Odd Extension with Signed Inner Conjugation in Biquaternionic Form__

## Introduction

A $\mathbb{Z}/2$-graded algebra is called a **superalgebra**, and the graded structure is part of the structure, not a decoration: it fixes the bracket, the derivation rule and the sign of every product. The physics series uses this framework in three places — the graded bracket of the Lie algebra, the fermion parity of the field, and the supercharge of supersymmetric quantum physics — and the purpose of this article is to state the framework once, to say exactly which part of it the biquaternion algebra supplies and which part must be adjoined, and to keep the several $\mathbb{Z}/2$'s of the corpus apart.

The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, which is the even part of the Clifford algebra of Minkowski space, $\mathbb{B}\cong\mathrm{Cl}^{+}_{1,3}$; the grading, the two slots and the parity reading are *The Graded Algebra, Fermion Parity and the Two Sectors with Signed Inner Conjugation in Biquaternionic Form*. The commutator bracket of the algebra, the trace form and the identification of the trace-free part with the Lorentz algebra are *Biquaternion Lie Algebra* and *Biquaternion Lie Group and Exponential*. The supercharge pair of the massive Dirac operator, the chirality grading of the two minimal left ideals and the warning that the supersymmetric grading is not the frame grading are *Supersymmetric Quantum Physics in the Biquaternion Framework*. The Grassmann algebra as the odd extension is *Grassmann Coherent States in Biquaternionic Form*, the ghost sector and its open question about a biquaternionic Grassmann envelope are *BRST Symmetry in Biquaternionic Form*, and the one fermionic mode that the algebra hosts natively, together with the three gradings warning, is *Fock Space and Creation/Annihilation Operators in Biquaternionic Form*. Nothing owned by those articles is re-derived; this article states the structure they share and the boundary of what the algebra carries.

## The Graded Commutator

**Definition.** A **$\mathbb{Z}/2$-graded algebra** is an algebra $A=A^0\oplus A^1$ with $A^iA^j\subseteq A^{i+j}$, written $\lvert a\rvert\in\{0,1\}$ for the parity of a homogeneous element. On it the **graded commutator** is

$$
[a,b]_{\mathrm{gr}}=ab-(-1)^{\lvert a\rvert\lvert b\rvert}\,ba .
$$

For two even elements it is the ordinary commutator; for one even and one odd element it is also the ordinary commutator; for two odd elements it is the **anticommutator** $\{a,b\}=ab+ba$. The single formula carries the whole fermionic sign convention: "bosons commute, fermions anticommute, and a boson and a fermion commute" is the parity of the exponent $(-1)^{\lvert a\rvert\lvert b\rvert}$ read three times.

**Proposition (the super-Jacobi identity).** On a graded algebra the graded commutator satisfies

$$
(-1)^{\lvert a\rvert\lvert c\rvert}[a,[b,c]_{\mathrm{gr}}]_{\mathrm{gr}}
+(-1)^{\lvert b\rvert\lvert a\rvert}[b,[c,a]_{\mathrm{gr}}]_{\mathrm{gr}}
+(-1)^{\lvert c\rvert\lvert b\rvert}[c,[a,b]_{\mathrm{gr}}]_{\mathrm{gr}}=0 ,
$$

the **graded Jacobi identity**, which is the ordinary Jacobi identity when all three elements are even and the identity of the anticommutator for three odd elements.

**Definition.** A **Lie superalgebra** is a graded algebra with a graded bracket that is graded antisymmetric, $[a,b]_{\mathrm{gr}}=-(-1)^{\lvert a\rvert\lvert b\rvert}[b,a]_{\mathrm{gr}}$, and satisfies the graded Jacobi identity. Its even part is a Lie algebra, its odd part is a module over the even part, and the bracket of two odd elements is even.

**Remark (a graded derivation).** The odd element that mixes the two components does so by a graded rule: a **graded derivation** $D$ of parity $\lvert D\rvert$ satisfies the graded Leibniz rule

$$
D(ab)=D(a)b+(-1)^{\lvert D\rvert\lvert a\rvert}a\,D(b),
$$

so an odd derivation differentiates with a sign that depends on the parity of the element it acts on. This is the rule a supercharge obeys, and it is the reason a supercharge cannot be written as an element of the even part alone.

## What Is a Grading of the Biquaternion Algebra?

The algebra is graded as a vector space by the Clifford grade, $\mathbb{B}=\mathbb{B}_0\oplus\mathbb{B}_1\oplus\mathbb{B}_2\oplus\mathbb{B}_3$ in the identification $\mathbb{B}\cong\mathrm{Cl}_{3,0}$, and under $\mathbb{B}\cong\mathrm{Cl}^{+}_{1,3}$ that grade is the bivector degree of the ambient algebra. The parity grading of the previous article is **not** the parity of that grade: it is the grading of the ambient algebra $\mathrm{Cl}_{1,3}$, on which the whole algebra $\mathbb{B}$ sits in the even slot.

**Proposition (the parity grading is trivial on the algebra).** The restriction of the parity grading of $\mathrm{Cl}_{1,3}$ to $\mathbb{B}=\mathrm{Cl}^0$ is the trivial grading: every element of the algebra is even. Consequently a $\mathbb{Z}/2$-grading of the algebra in which the familiar splitting plays the role of the parity is not supplied by the Clifford structure; the algebra alone carries no distinguished fermionic sector.

**Proof.** By definition $\mathrm{Cl}^0=\mathbb{B}$ and $\mathrm{Cl}^0\cap\mathrm{Cl}^1=\{0\}$, so the odd slot contains no element of the algebra.

**Remark (the gradings of the corpus do not coincide).** Three separate structures are called gradings in the series and they must not be conflated, as *Fock Space and Creation/Annihilation Operators in Biquaternionic Form* records: the sector splitting $\mathbb{M}_+\oplus\mathbb{M}_-$ by the Hermitian dagger, which grades the symmetrized product but is **not** an algebra grading, the counterexample being $(ie_1)(ie_2)=-e_3$; the number grading of the Fock space by total particle number, a grading of the state space; and the parity grading, an algebra grading of the ambient Clifford algebra. A fourth, the chirality $L/R$ grading of the two minimal left ideals, is the one the supersymmetry article uses, and the frame grading by $\beta$ is a fifth that must not be confused with it.

## The Graded Bracket with the Algebra as Even Part

**Proposition.** On $\mathrm{Cl}_{1,3}=\mathbb{B}\oplus\mathrm{Cl}^1$ the graded commutator satisfies

$$
[\mathbb{B},\mathbb{B}]_{\mathrm{gr}}\subseteq\mathbb{B},\qquad
[\mathbb{B},\mathrm{Cl}^1]_{\mathrm{gr}}\subseteq\mathrm{Cl}^1,\qquad
\{\mathrm{Cl}^1,\mathrm{Cl}^1\}\subseteq\mathbb{B},
$$

so the ambient algebra is a Lie superalgebra whose even part is $\mathbb{B}$ and whose odd part is a left and right module over it.

**Proof.** These are the inclusions $\mathrm{Cl}^i\mathrm{Cl}^j\subseteq\mathrm{Cl}^{i+j}$ of the grading, read with the parity of the exponent, together with the fact that the graded commutator of two elements of the same parity is their commutator and of two of opposite parity is also their commutator, while that of two odd elements is their anticommutator.

**Remark (the even part is the Lie algebra of the framework).** The restriction of the graded bracket to $\mathbb{B}$ is the ordinary commutator, that is the Lie algebra of *Biquaternion Lie Algebra*, whose trace-free part is the Lorentz algebra; the bivectors of the ambient algebra are its elements, and the identification with $\mathfrak{so}(1,3)$ and its spin representation is the one carried by the Clifford articles of the maths corpus. The odd slot is a module over the even part and not a second Lie algebra: the bracket of two odd elements is even, exactly as the bracket of two reflections is a rotation.

**Remark (the bracket of the two slots).** In the language of the previous article, the inclusion $[\mathbb{B},\mathrm{Cl}^1]\subseteq\mathrm{Cl}^1$ says that the bosonic sector acts on the fermionic one, and $\{\mathrm{Cl}^1,\mathrm{Cl}^1\}\subseteq\mathbb{B}$ says that two fermionic steps give a bosonic element. The graded bracket is therefore the abstract form of the composition table of the signed inner conjugation: the same table, read as a bracket instead of as a product.

## Supercharges and the Odd Generators

**Definition.** A **supercharge** is an odd element $Q$ of a Lie superalgebra whose graded square is even,

$$
\{Q,Q\}=2H,\qquad [Q,H]_{\mathrm{gr}}=0 ,
$$

so that the anticommutator of the supercharge with itself is a bosonic operator commuting with it. This is the structural content of supersymmetry: the symmetry is generated by an odd element, and the Hamiltonian is its square.

**Proposition (a supercharge is never an element of the algebra).** Since $\mathbb{B}=\mathrm{Cl}^0$ contains no odd element, no supercharge is an element of $\mathbb{B}$; every supercharge is an element of the odd slot of an ambient graded algebra, and the odd slot is isomorphic to $\mathbb{B}$ as a module but is not a subalgebra.

**Proof.** The odd slot is $\mathrm{Cl}^1$ and $\mathbb{B}=\mathrm{Cl}^0$, and the slots are disjoint by the grading; the module isomorphism is the one of the previous article.

**Remark (what the framework supplies and what it imports).** The corpus's supersymmetric quantum physics realizes a supercharge pair from the first-order biquaternion gradient $(\tilde{\nabla},\tilde{\nabla}^{\natural})$ and identifies the superalgebra with the mass pair; that construction is owned by *Supersymmetric Quantum Physics in the Biquaternion Framework*, together with the chirality grading of the two minimal left ideals under which the gradient is odd and the d'Alembertian even. What this article records is the general boundary: **the supercharge is fermionic, and fermionic elements are not in the algebra.** Whatever the algebra supplies for the pairing, the odd generator itself is an element of the Clifford slot that the algebra does not contain.

## What Must Be Adjoined

Two constructions in the series adjoin the missing odd sector, and both are honest about it.

**The Grassmann envelope.** The odd generators can be made to carry anticommuting coefficients by tensoring with a Grassmann algebra, which is exactly the construction of *Grassmann Coherent States in Biquaternionic Form*: the Grassmann algebra is the odd extension of the coefficient ring, and the Berezin integral is its integration. The resulting object is a superalgebra whose even part contains the algebra. *BRST Symmetry in Biquaternionic Form* uses the same envelope for the ghosts and records as an **open question** whether a biquaternionic Grassmann envelope can be found that is natural rather than imported; the question is open precisely because $\mathbb{B}$ supplies no odd elements of its own.

**One fermionic mode, natively.** The one piece of the odd sector that the algebra does host is a single fermionic mode: the creation and annihilation operators of one mode are elements of the algebra, the parity is the element $(-1)^F=ie_3$ of the informational sector, and the algebra's own graded structure therefore carries the finite one-mode case without any extension. This is the sharpest form of the boundary: the algebra hosts the parity of one mode and must import the parity of a field, for which the product $\prod_{\text{modes}}ie_3^{(\text{mode})}$ is not an element of $\mathbb{B}$.

**Remark (the count of what is adjoined).** One odd generator, and its products with the even elements, exhaust the odd slot: the odd part is the rank-one copy $\mathbb{B}\gamma$ of the algebra, generated over $\mathbb{B}$ by a single odd element $\gamma$. So the extension is not "one more algebra" but one more generator; two independent copies of the algebra are never needed, because the missing piece is a single module generator and the rule odd $\times$ odd $=$ even that it brings with it.

## One Graded Algebra, Not Two

**Proposition.** With one odd unit $\gamma$ one has $\mathrm{Cl}_{1,3}=\mathbb{B}\oplus\mathbb{B}\gamma$, and every supercharge is a $\mathbb{B}$-multiple of $\gamma$; the odd sector is a single module generator, not a second algebra.

**Proof.** The decomposition is the rank-two module statement of *The Graded Algebra, Fermion Parity and the Two Sectors with Signed Inner Conjugation in Biquaternionic Form*, and an odd element is $\gamma s$ with $s$ even, hence a $\mathbb{B}$-multiple of $\gamma$.

**Remark (why this is the answer to the "two copies" question).** A superalgebra needs an even part, an odd part and the graded bracket between them; it does not need two algebras. The pair $(\mathbb{B},\mathbb{B})$ of two independent copies has no bracket $\{\cdot,\cdot\}\to\mathbb{B}$ between the copies and no grading, so it is not a superalgebra. The single graded algebra $\mathrm{Cl}_{1,3}=\mathbb{B}\oplus\mathbb{B}\gamma$ has all three, and the biquaternion algebra is its even part.

## Honest Limits

- **The algebra is not a superalgebra by itself.** With the Clifford parity, the algebra is entirely even; with the chirality $L/R$ splitting, the two minimal left ideals give a $\mathbb{Z}/2$ of the module structure and not of the algebra. A statement that "the biquaternion algebra is a superalgebra" needs the ambient algebra or an explicit further grading, and this article does not make it.
- **The supercharge is imported.** The odd generator is not an element of $\mathbb{B}$; the Grassmann envelope or the odd slot of the Clifford algebra is required, and the naturality of that envelope is open in the BRST article.
- **The parity of a field is external.** $(-1)^F$ is an element of the algebra for one mode and a product over modes, hence outside it, for a field.
- **Nothing here is a measure or an integral.** The Grassmann and Berezin constructions are cited from their articles and are not used; the article is algebra and grading.
- **No supersymmetry algebra is claimed to be contained in $\mathbb{B}$.** The super-Poincaré algebra, if it is to be written, is written on an extension; the corpus's supersymmetry article states which superalgebra its construction realizes and this article adds the general boundary, not a second claim.

## Summary

A **superalgebra** is a $\mathbb{Z}/2$-graded algebra with the grading as part of its structure. On it the graded commutator $[a,b]_{\mathrm{gr}}=ab-(-1)^{\lvert a\rvert\lvert b\rvert}ba$ is the commutator for even or mixed pairs and the anticommutator for two odd elements, it satisfies the graded Jacobi identity, and a graded derivation obeys the graded Leibniz rule; that formula is the whole fermionic sign convention of the framework in one line. A Lie superalgebra has a Lie algebra as its even part, a module as its odd part, and the bracket of two odd elements in the even part.

The biquaternion algebra is the **even part** of the graded Clifford algebra, $\mathbb{B}=\mathrm{Cl}^0_{1,3}$, so the parity grading is trivial on it, and $\mathbb{B}$ is not by itself a superalgebra; the grading that the series calls parity is a grading of the ambient algebra, and it must not be conflated with the sector splitting by the dagger, which is not an algebra grading, with the chirality $L/R$ grading of the supersymmetry article, or with the number and frame gradings. The graded bracket makes the ambient algebra a Lie superalgebra with even part $\mathbb{B}$, whose even bracket is the Lie bracket of *Biquaternion Lie Algebra*, and the odd slot is a module generated by one odd element.

A **supercharge** is an odd element with $\{Q,Q\}=2H$, and it is therefore never an element of $\mathbb{B}$: the fermionic generator is an element of the odd slot, and the odd slot is the rank-one copy $\mathbb{B}\gamma$ of the algebra. The Grassmann envelope of the coherent-states and BRST articles adjoins the anticommuting coefficients, the naturality of that envelope being the open item those articles record; the algebra's own odd sector hosts one fermionic mode, $(-1)^F=ie_3$, and no more. One graded algebra with one extra odd generator suffices; two independent copies of the algebra would be a structure with no bracket between the copies and no grading, and are not what the physics needs.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A=A^0\oplus A^1$ | A $\mathbb{Z}/2$-graded algebra, a superalgebra |
| $\lvert a\rvert\in\{0,1\}$ | The parity of a homogeneous element |
| $[a,b]_{\mathrm{gr}}=ab-(-1)^{\lvert a\rvert\lvert b\rvert}ba$ | Graded commutator; anticommutator for two odd elements |
| graded Jacobi identity | The super-Jacobi identity of a Lie superalgebra |
| $D(ab)=D(a)b+(-1)^{\lvert D\rvert\lvert a\rvert}aD(b)$ | Graded Leibniz rule of a graded derivation |
| $\mathrm{Cl}_{1,3}=\mathbb{B}\oplus\mathrm{Cl}^1$ | Lie superalgebra, even part the biquaternion algebra |
| $\{\mathrm{Cl}^1,\mathrm{Cl}^1\}\subseteq\mathbb{B}$ | Two fermionic steps are bosonic |
| $\{Q,Q\}=2H$ | Supercharge; $Q$ odd, $H$ even |
| $\mathrm{Cl}^1=\mathbb{B}\gamma$ | One odd generator over the algebra, not a second algebra |
| $(-1)^F=ie_3$ | The one fermionic mode the algebra hosts natively |

## Further Reading

- Manfred Scheunert, *The Theory of Lie Superalgebras*, Lecture Notes in Mathematics 716 (Springer, 1979), for the graded bracket, the super-Jacobi identity and the structure theory.
- Julius Wess and Jonathan Bagger, *Supersymmetry and Supergravity* (Princeton University Press, 2nd ed. 1992), for the super-Poincaré algebra and the supercharge conventions.
- Bryce S. DeWitt, *Supermanifolds* (Cambridge University Press, 2nd ed. 1992), for the Grassmann envelope, the Berezin integral and the functorial view of the odd coordinates.
- Felix A. Berezin, *Introduction to Superanalysis* (Reidel, 1987), for the anticommuting coefficients and the algebra of the odd extension.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups*, Cambridge Studies in Advanced Mathematics 50 (Cambridge University Press, 1995), for the graded Clifford algebra, its even part and the parity of its elements.
