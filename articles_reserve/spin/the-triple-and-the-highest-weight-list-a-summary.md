# __The Triple and the Highest-Weight List Are Not Definitions of Spin: A Summary__

## Status

**The maths corpus has no definition of spin. We do not know what spin is, mathematically.** This file is the summary of the two candidates that were proposed as general algebra-level definitions and are now withdrawn: the spin triple and the highest-weight list. Every article that developed them has been moved into this directory.

The withdrawal is not a correction of a formula. The formulas are correct computations of weights. The error was to call a computation of a weight a definition of spin. A definition must say what spin is; a weight computation says what a grading element does on a carrier. The two are different objects.

**The only definition of spin in the corpus is physical.** Spin is the intrinsic angular momentum of a particle. In the rest frame the one-particle states satisfy

$$
\vec S^{\,2}\lvert s,m_s\rangle=\hbar^2s(s+1)\lvert s,m_s\rangle,\qquad
S_z\lvert s,m_s\rangle=\hbar\,m_s\lvert s,m_s\rangle,
$$

with $s\in\{0,\tfrac12,1,\tfrac32,2,\dots\}$ and $m_s=-s,\dots,s$. Relativistically $s$ labels the little-group $SU(2)$ representation carried by the time-like unitary irreducible representation of the Poincaré group; for a massless particle the invariant label is helicity. This definition belongs to the physics corpus. It is not derived from any algebra in this corpus, and no algebra in this corpus reproduces its three inputs: the rotation generator, the rest-frame one-particle space, and the unit $\hbar$.

## What the Algebra Actually Supplies

Let $A$ be a finite-dimensional unital algebra over a field of characteristic zero, $h\in A$ a grading element, and $(W,\rho)$ a carrier. The algebra supplies:

- the **weights** of $h$ on $W$, the eigenvalues of $\rho(h)$ counted with multiplicity;
- the **weight string**, the multiset of those eigenvalues;
- the **highest weight**, the largest eigenvalue for a chosen order;
- an **$\mathfrak{sl}_2$ triple** $(h,u,v)$ with $[h,u]=2u$, $[h,v]=-2v$ and $[u,v]=h$, when the brackets close;
- the **irreducible modules** $W_j$ of that triple, of dimension $2j+1$ and weights $j,j-1,\dots,-j$.

These are standard representation theory. They are correct. They are not a definition of spin, because none of them names a physical quantity. The passage from the highest weight $j$ to the spin requires the identification $h=2S_z/\hbar$, the identification of $\rho$ with the rotation action, and the identification of $W$ with the rest-frame one-particle space. Those three identifications are physical hypotheses. They are not supplied by $A$, by $h$, or by the triple.

## The Triple as a General Definition

**The proposal.** For every finite-dimensional algebra $A$, define the spin list as the set of spins $j$ of the irreducible carriers of every $\mathfrak{sl}_2$ triple contained in $A$ (or in $A\otimes_{\mathbb{R}}\mathbb{C}$). On $M_2(\mathbb{C})$ this returns $\{0,\tfrac12,1\}$: the centre, the defining module and the traceless part of the adjoint.

**Why it is not a definition.**

1. **The triple is extra data.** A general algebra contains no canonical $\mathfrak{sl}_2$ triple. $M_n(\mathbb{C})$ contains a principal triple, a balanced Peirce triple for even $n$, and many others. They give different lists. The definition therefore depends on a choice that the algebra does not make.
2. **The list is not a function of the algebra.** Two triples in the same algebra give different lists. A definition of an object of the algebra must not depend on an arbitrary choice of triple.
3. **It fails outside $M_2(\mathbb{C})$.** For $n>2$ the principal triple gives $(n-1)/2$, not a value selected by the physics. The Peirce root of a primitive idempotent closes to an $\mathfrak{sl}_2$ only at $n=2$; this is the algebraic accident that made the biquaternion case look canonical.
4. **It returns representation labels, not spins.** The output is the set of highest weights of the chosen triples. Calling those numbers spins is the identification that has to be justified, and it cannot be justified from the algebra alone.
5. **Commutative algebras have no triple.** The definition is silent on them, or returns the empty set. That is not a defect of those algebras; it shows that the triple is an added structure.

**What survives.** The triple is a legitimate object of representation theory. The article *Representations of Lie Algebras* and the standard theory of $\mathfrak{sl}_2$ remain. The claim that the triple defines spin does not survive.

## The Highest-Weight List as a General Definition

**The proposal.** For a fixed algebra $A$, take a natural family of carriers (the centre, the defining module, the adjoint, and their tensor constructions), read the highest weight of a chosen grading element on each, and call the resulting set the spin list. On $M_2(\mathbb{C})$ this returns $\{0,\tfrac12,1\}$.

**Why it is not a definition.**

1. **It is a list of top weights.** The output is $\{\lambda_{\max}(\rho(h|_W))/2\}$ over a selected family $W$. The selection of the family is extra data, and the normalisation by $2$ is a convention imported from the $\mathfrak{sl}_2$ case.
2. **It agrees with the triple only where the family is the triple's modules.** At $M_2(\mathbb{C})$ the natural family is exactly the three carriers of the triple. Above $M_2(\mathbb{C})$ the family and the triple diverge. The agreement at $n=2$ is the coincidence, not the rule.
3. **The list is not closed under the operations of the algebra.** Tensor products, direct sums and quotients change the list in a way that no single algebraic definition controls.
4. **It is either finite by an arbitrary cut or infinite.** Without a cut, every $j\ge0$ occurs over all modules; with a cut, the cut is the definition, not the algebra.

**What survives.** The highest weight is a correct invariant of a carrier. The article *Representations of Lie Algebras* remains. The claim that the highest-weight list defines spin does not survive.

## The Other Two Candidates

The reserve article *Possible General Definitions of the Spin of an Algebra* also examined the module list and the orbit list. Both are withdrawn for the same reason.

- The **module list** reads $\dim W$ and returns $(\dim W-1)/2$. At $M_2(\mathbb{C})$ it gives $\{0,\tfrac12,1\}$ only because the natural family happens to have dimensions $1,2,3$. Above $M_2(\mathbb{C})$ it returns half the dimension of the adjoint, not the adjoint highest weight: $\tfrac72$ at $M_3$, $\tfrac{23}{2}$ at $M_5$.
- The **orbit list** reads coadjoint orbits. It is overcomplete already at $M_3(\mathbb{C})$ and it requires a choice of orbit and a symplectic normalisation.

Neither is a definition of spin.

## Why the $M_2(\mathbb{C})$ Test Misled

The test was: a definition is pertinent if it returns exactly $\{0,\tfrac12,1\}$ on $M_2(\mathbb{C})$. The test is necessary for matching the three observed values of the biquaternion sector. It is not sufficient, for three reasons.

1. **At $M_2(\mathbb{C})$ the semisimple part is $\mathfrak{sl}_2$.** The adjoint is the defining module, the Casimir is $j(j+1)$, and the highest weight is the spin of the triple by construction. Every formula that is correct for $\mathfrak{sl}_2$ passes.
2. **The test selects by the answer.** It accepts any method that happens to produce the three numbers. A fit is not a definition.
3. **The next case rejects the fit.** The Casimir list passes the test and returns $0.758$ and $1.303$ at $M_3(\mathbb{C})$. The module list and the orbit list pass at $M_2$ and fail above it. Passing at $M_2$ is an accident of the smallest semisimple case.

## The Four Halves, Kept Apart

The symbol $\tfrac12$ occurs in four roles in the withdrawn material. None of them is a definition of spin.

| occurrence | what it is | what it is not |
|---|---|---|
| $j=\lambda_{\max}/2$ | conversion from root weight to highest-weight label | not a definition of spin |
| $S=\tfrac12[U,V]$ | antisymmetrisation of the product | not a normalisation of spin |
| $\theta/2$ in $\exp(\theta h/2)$ | exponential coordinate of the rotor | not the spin |
| $J_k=\tfrac12\operatorname{ad}_{i\vec e_k}$ | Hermitian normalisation of the adjoint generator | not a half-angle |

## What Remains in the Maths Corpus

The maths corpus keeps the following, and none of them defines spin.

- **Weight theory.** Grading elements, weights, weight strings, highest weights, the Peirce weight table.
- **$\mathfrak{sl}_2$ representation theory.** Triples, ladder operators, irreducible modules, the Clebsch–Gordan decomposition. The triple is studied as a Lie-algebra object, not as a definition of spin.
- **Peirce decomposition and spinors.** Idempotents, corners, minimal left ideals, the spinor as a coordinate. A spinor is a coordinate on a carrier; it is not a spin.
- **Spin groups and Clifford modules.** $\mathrm{Spin}(n)$, $\mathrm{Pin}(n)$, Clifford modules and their representations. These are groups and representations, not the spin quantum number. The word *spin* in their names is historical.
- **Chirality.** The central sign $\chi=i\tilde\Xi_{\mathrm{ad}}$ of the biquaternion complexification, which grades $S$ against $S^{\mathrm{c}}$. It is not a spin and not a Peirce index.

**The rule.** No article in `articles_maths` states a mathematical definition of spin. When the weight of a grading element is meant, the article writes *highest weight* or *weight*, not *spin*. The word *spin* in the maths corpus is reserved for the names of the spin group and the spinor, which are different objects, and for citations of the physics corpus.

## The Inventory of This Directory

| file | what it contains | why it is here |
|---|---|---|
| `the-general-definition-of-spin.md` | the triple, the pair, the structure theorem, the principal chains | proposed the triple as the general definition |
| `the-weight-of-a-frame-root-and-the-spin-quantum-number.md` | frame root, carrier, weight, highest weight, Peirce weights | proposed the highest-weight reading as the definition |
| `the-spin-of-a-biquaternion.md` | the frame pair, the three elementary carriers, the half-angle | declared the highest-weight computation the single definition |
| `the-approaches-to-spin-weight-half-angle-ladder-and-adjoint.md` | synthesis of the four readings | presented the four readings as approaches to spin |
| `the-spin-chain-and-the-adjoint-decomposition-mnc.md` | the principal chain of $M_n(\mathbb{C})$ | reads the chain as a spin ladder |
| `the-spin-chain-and-the-adjoint-decomposition-of-m3c.md` | the $M_3(\mathbb{C})$ chain | same, at $n=3$ |
| `the-spin-chain-and-the-adjoint-decomposition-of-m4c.md` | the $M_4(\mathbb{C})$ chain | same, at $n=4$ |
| `the-spin-chain-and-the-adjoint-decomposition-of-m5c.md` | the $M_5(\mathbb{C})$ chain | same, at $n=5$ |
| `the-spin-chain-and-the-adjoint-decomposition-of-m6c.md` | the $M_6(\mathbb{C})$ chain | same, at $n=6$ |
| `the-spin-two-chain-and-the-adjoint-of-m5c.md` | the spin-two chain of $M_5(\mathbb{C})$ | same, at $n=5$, spin two |
| `the-triplet-spin-one-and-the-adjoint-of-m3c.md` | the triplet and the adjoint of $M_3(\mathbb{C})$ | same, at $n=3$, spin one |
| `the-general-definitions-of-the-spin-of-an-algebra.md` | the four candidates and their divergence | the general-definition programme |
| `the-dubious-definitions-of-the-spin-of-an-algebra.md` | quarantine of the failed methods | the audit of the programme |
| `the-incomplete-definitions-of-the-spin-of-an-algebra.md` | the methods that fail the $M_2(\mathbb{C})$ test | the audit, Part I |
| `the-principal-pair-of-m2c-a-worked-computation.md` | worked principal pair of $M_2(\mathbb{C})$ | the principal-pair computations |
| `the-principal-pair-of-m3c-a-worked-computation.md` | worked principal pair of $M_3(\mathbb{C})$ | same, at $n=3$ |
| `the-principal-pair-of-m4c-a-worked-computation.md` | worked principal pair of $M_4(\mathbb{C})$ | same, at $n=4$ |
| `the-principal-pair-of-m5c-a-worked-computation.md` | worked principal pair of $M_5(\mathbb{C})$ | same, at $n=5$ |
| `the-spin-of-the-complex-numbers-the-absence-of-a-pair.md` | $\mathbb{C}$ has no pair | the case study of a spinless algebra |
| `the-spin-of-the-quaternion-algebra-a-worked-computation.md` | $\mathbb{H}$ over $\mathbb{R}$ and $\mathbb{C}$ | the case study of the division algebra |
| `the-spin-of-the-split-complex-numbers-a-root-without-a-ladder.md` | $\mathbb{D}$ has a root but no ladder | the case study of the split algebra |

The files are kept because their computations of weights, dimensions and decompositions are correct and may be useful. They are quarantined because their titles and conclusions call those computations spins.

## The Honest Statement

**We have no mathematical definition of spin.** We have a physical definition, a family of correct weight computations, and a set of names that the physics gives to the numbers those computations produce. The passage from the computation to the physical number is not a theorem of the corpus. It is an identification, and the corpus has not justified it.

Any future mathematical definition of spin must state what object it defines, on which space, with which action, and why that object is the spin of a particle. Until then, the maths corpus computes weights. It does not define spin.
