# __The Superalgebra Reading and the Odd Extension with Signed Hermitian Adjoint in Biquaternionic Form__

## Introduction

The biquaternion algebra is the even part of the graded Clifford algebra, $\mathbb{B}=\mathrm{Cl}^0_{1,3}$, and the graded commutator $[a,b]_{\mathrm{gr}}=ab-(-1)^{\lvert a\rvert\lvert b\rvert}ba$ makes the ambient algebra a Lie superalgebra whose even part is the algebra of the series. That structure is built from the product and the parity, and it is what *The Superalgebra Reading and the Odd Extension with Signed Inner Conjugation in Biquaternionic Form* develops, together with the supercharge, the Grassmann envelope and the boundary of what the algebra supplies and what it imports.

This article is the **Hermitian reading** of the same structure. A superalgebra used by physics does not carry only a bracket; it carries an **adjoint**, the operation that turns a state into a dual state and an operator into its Hermitian conjugate, and it is the adjoint that makes the Hamiltonian Hermitian and the probability real. In the inverse reading the odd sector is reached through the inverse of a parameter, which belongs to the group of units; here it is reached through the Hermitian adjoint $X^{*}$, the adjoint of the spinor form of the framework. The object of the article is the interaction of the two: a $\mathbb{Z}/2$-graded algebra with a parity-preserving anti-involution, and the sign it puts on the graded bracket.

Three statements carry the reading. The first is that the dagger is an **even anti-involution** of the superalgebra, $(ab)^{*}=b^{*}a^{*}$ with $\lvert a^{*}\rvert=\lvert a\rvert$; it is the structure the corpus's own physics uses, since the biquaternionic supercharge is paired with its adjoint, $\{Q,Q^{*}\}=H$, in *Supersymmetric Quantum Mechanics in the Biquaternion Framework*. The second is that the adjoint **reverses the graded bracket** up to the parity sign,

$$
\bigl([a,b]_{\mathrm{gr}}\bigr)^{*}=-(-1)^{\lvert a\rvert\lvert b\rvert}\,\bigl[a^{*},b^{*}\bigr]_{\mathrm{gr}},
$$

so it reverses a commutator and preserves an anticommutator, the reason being that it reverses the order of the factors and the two graded signs then contribute in opposite directions. The third is that this is a statement about the *convention*: the Koszul-signed rule of a super-* would make the adjoint an anti-automorphism of the bracket without the extra sign, and the corpus's dagger does not obey that rule; the two conventions are distinguished by a check on two generators, and the article records which one the physics uses.

The graded bracket, the parity table, the Lie-superalgebra statement and the odd extension are the ones of the inverse article and are restated only where the Hermitian structure changes them; the parity reading of the ambient algebra and the sectors are *The Graded Algebra, Fermion Parity and the Two Sectors with Signed Hermitian Adjoint in Biquaternionic Form*; the supercharge pair and the chirality grading are *Supersymmetric Quantum Mechanics in the Biquaternion Framework*; the Grassmann envelope is *Grassmann Coherent States in Biquaternionic Form* and *BRST Symmetry in Biquaternionic Form*; the commutator bracket and the trace-free part are *Biquaternion Lie Algebra*; the one-mode parity is *Fock Space and Creation/Annihilation Operators in Biquaternionic Form*. Nothing owned by those articles is re-derived.

**Conventions.** $\mathrm{Cl}_{1,3}$ is the ambient Clifford algebra of Minkowski space in the mostly-minus convention, $\mathbb{B}=\mathrm{Cl}^0_{1,3}$ its even part, $\gamma^\mu$ the odd generators; the grading is by parity, $\lvert a\rvert\in\{0,1\}$; the graded commutator is $[a,b]_{\mathrm{gr}}=ab-(-1)^{\lvert a\rvert\lvert b\rvert}ba$, the commutator for even or mixed pairs and the anticommutator for two odd elements; the dagger is the Hermitian adjoint of the algebra, extended to the envelope by $X^{*}=\sigma(\alpha(X^{r}))$ as in the companion article, so that $(ab)^{*}=b^{*}a^{*}$ and $\lvert a^{*}\rvert=\lvert a\rvert$.

## The Graded Commutator

**Definition.** On a $\mathbb{Z}/2$-graded algebra $A=A^0\oplus A^1$ the **graded commutator** is

$$
[a,b]_{\mathrm{gr}}=ab-(-1)^{\lvert a\rvert\lvert b\rvert}ba ,
$$

the two parities read modulo two. It is the commutator on an even or a mixed pair and the anticommutator on two odd elements, and it satisfies the graded Jacobi identity, making a Lie superalgebra of the graded algebra with the graded commutator as bracket.

**Proposition (the parity of the bracket).** For homogeneous $a,b$ the bracket is even,

$$
\bigl\lvert[a,b]_{\mathrm{gr}}\bigr\rvert=\lvert a\rvert+\lvert b\rvert \pmod 2 ,
$$

so the bracket of two odd elements is even, the bracket of an even and an odd element is odd, and the bracket of two even elements is even. On the ambient Clifford algebra,

$$
[\mathbb{B},\mathbb{B}]\subseteq\mathbb{B},\qquad
[\mathbb{B},\mathrm{Cl}^1]\subseteq\mathrm{Cl}^1,\qquad
\{\mathrm{Cl}^1,\mathrm{Cl}^1\}\subseteq\mathbb{B}.
$$

**Proof.** These are the inclusions $\mathrm{Cl}^i\mathrm{Cl}^j\subseteq\mathrm{Cl}^{i+j}$ of the grading, read with the parity of the exponent, together with the fact that the graded commutator of two elements of the same parity is their commutator and of two of opposite parity is also their commutator, while that of two odd elements is their anticommutator.

**Remark (the even part is the Lie algebra of the framework).** The restriction of the graded bracket to $\mathbb{B}$ is the ordinary commutator, that is the Lie algebra of *Biquaternion Lie Algebra*, whose trace-free part is the Lorentz algebra. The odd slot is a module over the even part and not a second Lie algebra: the bracket of two odd elements is even, exactly as the bracket of two reflections is a rotation.

## The Adjoint of the Graded Bracket

**Proposition (the dagger is an even anti-involution of the superalgebra).** The Hermitian adjoint satisfies

$$
(ab)^{*}=b^{*}a^{*},\qquad (a^{*})^{*}=a,\qquad
\lvert a^{*}\rvert=\lvert a\rvert ,
$$

so it is an anti-automorphism of the graded algebra and it preserves the grading; it is $\mathbb{C}$-antilinear in each factor.

*Proof.* The reversion reverses the order of the factors, the grade involution acts on the degree and not on the order, and the coefficient conjugation is a $\mathbb{C}$-antilinear automorphism acting on the coefficients only; the composite therefore reverses the order and preserves the degree, so it is an anti-automorphism, involutive and even. On the algebra this is the Hermitian conjugation \tilde{Q}^{*}=\overline{\tilde{Q}^{\natural}} of the corpus.

**Proposition (the adjoint reverses a commutator and preserves an anticommutator).** For homogeneous $a,b$,

$$
\bigl([a,b]_{\mathrm{gr}}\bigr)^{*}=-(-1)^{\lvert a\rvert\lvert b\rvert}\,\bigl[a^{*},b^{*}\bigr]_{\mathrm{gr}},
$$

that is

$$
\bigl([a,b]_{\mathrm{gr}}\bigr)^{*}=
\begin{cases}
-\,\bigl[a^{*},b^{*}\bigr]_{\mathrm{gr}}, & a,b\ \text{not both odd},\\[2pt]
+\,\bigl[a^{*},b^{*}\bigr]_{\mathrm{gr}}, & a,b\ \text{both odd}.
\end{cases}
$$

*Proof.* Apply the anti-automorphism to the definition: $\bigl([a,b]_{\mathrm{gr}}\bigr)^{*}=(ab)^{*}-(-1)^{\lvert a\rvert\lvert b\rvert}(ba)^{*}=b^{*}a^{*}-(-1)^{\lvert a\rvert\lvert b\rvert}a^{*}b^{*}$. Since $\lvert a^{*}\rvert=\lvert a\rvert$ and $\lvert b^{*}\rvert=\lvert b\rvert$, the same exponent occurs in $\bigl[a^{*},b^{*}\bigr]_{\mathrm{gr}}=a^{*}b^{*}-(-1)^{\lvert a\rvert\lvert b\rvert}b^{*}a^{*}$, and the two expressions differ by the factor $-(-1)^{\lvert a\rvert\lvert b\rvert}$; for $a,b$ both odd the factor is $+1$, and otherwise it is $-1$. The identity was checked on the generators $\gamma^{\mu}$ and on products of two of them, for all four parity pairs.

**Remark (why the two behave differently).** The adjoint reverses the order of the two factors, and the graded bracket distinguishes the two orders by the sign $(-1)^{\lvert a\rvert\lvert b\rvert}$ exactly in the odd-odd case, where the bracket is symmetric: a symmetric bracket is preserved by the reversal, an antisymmetric one is negated. The statement is therefore not an accident of the Clifford algebra but the interaction of two signs, the order reversal of the adjoint and the Koszul sign of the bracket. On the even part, where the bracket is the Lie bracket of the framework, the rule reads $\bigl([a,b]\bigr)^{*}=-\bigl[a^{*},b^{*}\bigr]$, so the bracket of two anti-Hermitian elements is anti-Hermitian: the anti-Hermitian part is a Lie subalgebra, the compact form of the framework, while the Hermitian generators enter it with the conventional factor $i$.

**Remark (the Koszul-signed convention and what the dagger is not).** A superalgebra is often equipped with a super-* satisfying the Koszul-signed rule $(ab)^{*}=(-1)^{\lvert a\rvert\lvert b\rvert}b^{*}a^{*}$. For such a structure the bracket-adjoint identity reads $\bigl([a,b]_{\mathrm{gr}}\bigr)^{*}=-\bigl[a^{*},b^{*}\bigr]_{\mathrm{gr}}$ without the extra parity sign. The dagger of the corpus is **not** of that kind: on two generators $\gamma^0,\gamma^1$, both odd, one has $(\gamma^0\gamma^1)^{*}=\gamma^1\gamma^0=-\gamma^0\gamma^1$, while the Koszul-signed expression would be $(-1)^{1\cdot1}\gamma^1\gamma^0=+\gamma^0\gamma^1$. The corpus's dagger is the plain anti-involution, and the factor $(-1)^{\lvert a\rvert\lvert b\rvert}$ in the bracket identity is the price of it. A reader importing the super-* convention from the supersymmetry literature must choose which of the two signs his own dagger obeys, and the two are not the same map.

## Supercharges, the Adjoint and the Odd Generators

**Definition.** A **supercharge** is an odd element $Q$ of a Lie superalgebra whose graded square is even,

$$
\{Q,Q\}=2H,\qquad [Q,H]_{\mathrm{gr}}=0 ,
$$

so that the anticommutator of the supercharge with itself is a bosonic operator commuting with it. In the Hermitian reading the pairing used by the physics is the one with the **adjoint** rather than with the element itself,

$$
\{Q,Q^{*}\}=2H ,
$$

which is the convention of *Supersymmetric Quantum Mechanics in the Biquaternion Framework*, $\{Q,Q^{*}\}=H$, $Q^{2}=(Q^{*})^{2}=0$ in the nilpotent realisation of the flat theory. The two displays coincide in the real forms in which $Q^{*}$ is identified with $Q$, and the numerical factor between the two conventions is a normalisation.

**Proposition (the adjoint pairing is Hermitian and even).** If $Q$ is odd then $Q^{*}$ is odd and

$$
\{Q,Q^{*}\}=QQ^{*}+Q^{*}Q
$$

is even and Hermitian, $\{Q,Q^{*}\}^{*}=\{Q,Q^{*}\}$; a supercharge is never an element of $\mathbb{B}$.

*Proof.* The dagger preserves the parity, so $Q^{*}$ is odd and the product of two odd elements is even; the anticommutator of two elements and the adjoint of a product give $\{Q,Q^{*}\}^{*}=(QQ^{*}+Q^{*}Q)^{*}=QQ^{*}+Q^{*}Q$ by the anti-automorphism property. Since $\mathbb{B}=\mathrm{Cl}^0$ contains no odd element, no supercharge is an element of the algebra.

**Remark (why the adjoint and not the inverse).** The Hamiltonian of the framework must be Hermitian, and its spectrum real, and the pairing $\{Q,Q^{*}\}$ is Hermitian automatically because the adjoint is an adjoint; a pairing built with the inverse, $\{Q,Q^{-1}\}$, has no reason to be. This is the physical content of the Hermitian reading of the odd sector: the operator that pairs the two chiralities is the adjoint of the supercharge and not its inverse, and the corpus's own supersymmetric realisation of the mass pair is written with the dagger for that reason. The difference between the two pairings is a norm, $X^{*}=\sigma(N(X))\sigma(X)^{-1}$, so on the unit slice of the real quaternions they coincide and elsewhere they differ by a scalar; the commutator structure below is insensitive to it, which is the honest scope of the distinction.

**Remark (the supercharge in the module).** The odd slot is the rank-one module $\mathrm{Cl}^1=\mathbb{B}\gamma$, so an odd element is $Q=s\gamma$ with $s$ even. By the anti-automorphism property its adjoint is

$$
Q^{*}=(s\gamma)^{*}=\gamma^{*}s^{*}=-\gamma\,s^{*},
$$

an odd element again, and

$$
Q\,Q^{*}=-q(\gamma)\,s\,s^{*},
$$

an even element whose Hermitian part is the pairing of the supercharge with its adjoint. When the even element $s$ is built from the generators orthogonal to $\gamma$ — so that $\gamma$ commutes with it — the anticommutator is the symmetric expression $\{Q,Q^{*}\}=-q(\gamma)(ss^{*}+s^{*}s)$, which is the form the Hamiltonian takes in the one-mode case. The general anticommutator is even and Hermitian by the previous proposition; the symmetric formula is not claimed beyond the case in which the commutation holds, because a generator need not commute with an even element.

## What Must Be Adjoined

Two constructions in the series adjoin the missing odd sector, and in the Hermitian reading each has to be compatible with the adjoint.

**The Grassmann envelope.** The odd generators can be made to carry anticommuting coefficients by tensoring with a Grassmann algebra, the construction of *Grassmann Coherent States in Biquaternionic Form*; *BRST Symmetry in Biquaternionic Form* uses the same envelope for the ghosts and records as an **open question** whether a biquaternionic envelope can be found that is natural rather than imported. In the Hermitian reading the question acquires a second clause: the envelope must carry an involution compatible with the dagger of the algebra, since a Berezin integral and a Hilbert structure must be defined on the same object. The Grassmann algebra does carry one — the coefficient conjugation extended to the odd coefficients — and that is the envelope the physics uses; what is open is its naturality, not its existence.

**One fermionic mode, natively.** The one piece of the odd sector that the algebra does host is a single fermionic mode: the creation and annihilation operators of one mode are elements of the algebra, the parity is the element $(-1)^F=ie_3$ of the informational sector, and the algebra's own graded structure therefore carries the finite one-mode case without any extension. The parity operator is Hermitian, $(-1)^F\in\mathbb{M}_+$, as a parity operator of a unitary theory must be; the parity of a field, $\prod_{\text{modes}}ie_3^{(\text{mode})}$, is not an element of the algebra.

**Remark (the count of what is adjoined).** One odd generator, and its products with the even elements, exhaust the odd slot: the extension is not "one more algebra" but one more generator, and the rule odd $\times$ odd $=$ even that it brings with it.

## One Graded Algebra, Not Two

**Proposition.** With one odd unit $\gamma$ one has $\mathrm{Cl}_{1,3}=\mathbb{B}\oplus\mathbb{B}\gamma$, every supercharge is a $\mathbb{B}$-multiple of $\gamma$, and the odd slot carries the Hermitian form induced by the module structure, $\langle s\gamma,t\gamma\rangle=-q(\gamma)\langle s,t\rangle$ with $\langle s,t\rangle=\mathrm{Sc}(s^{*}t)$ and $\langle s,t\gamma\rangle=0$ for even $s,t$.

**Proof.** The decomposition is the rank-two module statement of *The Graded Algebra, Fermion Parity and the Two Sectors with Signed Hermitian Adjoint in Biquaternionic Form*, and an odd element is $\gamma s$ with $s$ even. For the form, $\gamma^{*}=-\gamma$, so $(s\gamma)^{*}(t\gamma)=-\gamma s^{*}t\gamma$ and the scalar part of $\gamma w\gamma$ for even $w$ is $q(\gamma)\mathrm{Sc}(w)$, which was checked on the four generators and on even samples; the orthogonality is the vanishing of the scalar part of an odd element. The elementwise identity without the scalar part is false — a generator need not commute with an even element — and the claim is made only for the form.

**Remark (why this is the answer to the "two copies" question).** A superalgebra needs an even part, an odd part, the graded bracket between them and the adjoint; it does not need two algebras. The pair $(\mathbb{B},\mathbb{B})$ of two independent copies has no bracket $\{\cdot,\cdot\}\to\mathbb{B}$ between the copies, no grading and no adjoint pairing across them, so it is not a superalgebra. The single graded algebra $\mathrm{Cl}_{1,3}=\mathbb{B}\oplus\mathbb{B}\gamma$ has all of them, and the biquaternion algebra is its even part.

## Honest Limits

- **The algebra is not a superalgebra by itself.** With the Clifford parity the algebra is entirely even; with the chirality $L/R$ splitting the two minimal left ideals give a $\mathbb{Z}/2$ of the module structure and not of the algebra. The statement that "the biquaternion algebra is a superalgebra" needs the ambient algebra or an explicit further grading, and this article does not make it.
- **The supercharge is imported.** The odd generator is not an element of $\mathbb{B}$; the Grassmann envelope or the odd slot of the Clifford algebra is required, and the naturality of that envelope is open in the BRST article.
- **The parity of a field is external.** $(-1)^F$ is an element of the algebra for one mode and a product over modes, hence outside it, for a field.
- **The dagger of the envelope is a convention.** The corpus defines the Hermitian dagger on the algebra; the extension used here, $X^{*}=\sigma(\alpha(X^{r}))$, is the one of the maths corpus and agrees with the algebra's dagger on the even part. The reversion is the other natural anti-involution of the envelope, and the bracket-adjoint identity holds for it as well, because it is a property of any parity-preserving anti-involution; only the identification of the involution with the physical adjoint depends on the choice, and the reversion is not the adjoint of the spinor form.
- **Nothing here is a measure or an integral.** The Grassmann and Berezin constructions are cited from their articles and are not used; the article is algebra, grading and adjointness.
- **No supersymmetry algebra is claimed to be contained in $\mathbb{B}$.** The super-Poincaré algebra, if it is to be written, is written on an extension; the corpus's supersymmetry article states which superalgebra its construction realizes, and this article adds the general boundary and the Hermitian structure, not a second claim.

## Summary

A **superalgebra** is a $\mathbb{Z}/2$-graded algebra with the grading as part of its structure, and on it the graded commutator $[a,b]_{\mathrm{gr}}=ab-(-1)^{\lvert a\rvert\lvert b\rvert}ba$ is the commutator for even or mixed pairs and the anticommutator for two odd elements. The biquaternion algebra is the **even part** of the graded Clifford algebra, $\mathbb{B}=\mathrm{Cl}^0_{1,3}$, so it is not by itself a superalgebra, and it must not be conflated with the chirality grading of the supersymmetry article or with the sector splitting by the dagger.

Read with the **Hermitian adjoint**, the superalgebra carries an even anti-involution, $(ab)^{*}=b^{*}a^{*}$ with $\lvert a^{*}\rvert=\lvert a\rvert$, and the adjoint of the graded bracket is

$$
\bigl([a,b]_{\mathrm{gr}}\bigr)^{*}=-(-1)^{\lvert a\rvert\lvert b\rvert}\bigl[a^{*},b^{*}\bigr]_{\mathrm{gr}},
$$

so it reverses a commutator and preserves an anticommutator: the adjoint reverses the order of the factors, and only the odd-odd, symmetric case is even under the reversal. The Koszul-signed super-* convention would give the cleaner rule without the parity sign, and the corpus's dagger is not of that convention; the two are distinguished on two generators.

A **supercharge** is an odd element; it is paired with its **adjoint**, $\{Q,Q^{*}\}=2H$, which is Hermitian and even because the adjoint is an adjoint, this being the pairing of the corpus's supersymmetric quantum mechanics and the reason the Hamiltonian is real. In the module $\mathrm{Cl}^1=\mathbb{B}\gamma$ a supercharge is $Q=s\gamma$ with adjoint $Q^{*}=-\gamma s^{*}$ and $QQ^{*}=-q(\gamma)ss^{*}$, an even element; the symmetric form of the self-pairing is claimed only when the generator commutes with $s$. The odd extension is one generator, not a second algebra, and the odd slot carries the algebra's own Hermitian form.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A=A^0\oplus A^1$ | A $\mathbb{Z}/2$-graded algebra, a superalgebra |
| $\lvert a\rvert\in\{0,1\}$ | The parity of a homogeneous element |
| $[a,b]_{\mathrm{gr}}=ab-(-1)^{\lvert a\rvert\lvert b\rvert}ba$ | Graded commutator; anticommutator for two odd elements |
| graded Jacobi identity | The super-Jacobi identity of a Lie superalgebra |
| $\mathrm{Cl}_{1,3}=\mathbb{B}\oplus\mathrm{Cl}^1$ | Lie superalgebra, even part the biquaternion algebra |
| $\{\mathrm{Cl}^1,\mathrm{Cl}^1\}\subseteq\mathbb{B}$ | Two fermionic steps are bosonic |
| $X^{*}=\sigma(\alpha(X^{r}))$ | The Hermitian adjoint; even anti-involution of the superalgebra |
| $\bigl([a,b]_{\mathrm{gr}}\bigr)^{*}=-(-1)^{\lvert a\rvert\lvert b\rvert}[a^{*},b^{*}]_{\mathrm{gr}}$ | The adjoint reverses a commutator, preserves an anticommutator |
| $(ab)^{*}=(-1)^{\lvert a\rvert\lvert b\rvert}b^{*}a^{*}$ | The Koszul-signed super-*; **not** the dagger of the corpus |
| $\{Q,Q^{*}\}=2H$ | Supercharge paired with its adjoint; Hermitian and even |
| $Q=s\gamma$, $Q^{*}=-\gamma s^{*}$, $QQ^{*}=-q(\gamma)ss^{*}$ | The supercharge in the module $\mathrm{Cl}^1=\mathbb{B}\gamma$ |
| $\langle s\gamma,t\gamma\rangle=-q(\gamma)\langle s,t\rangle$, $\langle s,t\gamma\rangle=0$ | The Hermitian form on the odd slot ($\langle s,t\rangle=\mathrm{Sc}(s^{*}t)$) |
| $(-1)^F=ie_3\in\mathbb{M}_+$ | The one fermionic mode the algebra hosts natively |

## Further Reading

- Manfred Scheunert, *The Theory of Lie Superalgebras*, Lecture Notes in Mathematics 716 (Springer, 1979), for the graded bracket, the super-Jacobi identity and the structure theory.
- Julius Wess and Jonathan Bagger, *Supersymmetry and Supergravity* (Princeton University Press, 2nd ed. 1992), for the super-Poincaré algebra and the supercharge conventions.
- Bryce S. DeWitt, *Supermanifolds* (Cambridge University Press, 2nd ed. 1992), for the Grassmann envelope, the Berezin integral and the functorial view of the odd coordinates.
- Felix A. Berezin, *Introduction to Superanalysis* (Reidel, 1987), for the anticommuting coefficients and the algebra of the odd extension.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for the involutions of a Clifford algebra, the adjoint of an anti-automorphism and the unitary groups they define.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups*, Cambridge Studies in Advanced Mathematics 50 (Cambridge University Press, 1995), for the graded Clifford algebra, its even part and the parity of its elements.
